#!/usr/bin/env python
"""
Performs basic cleaning on the data and save the results in Weights & Biases
"""
import argparse
from ast import arg
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    logger.info("Downloading artifact")
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    logger.info("Create panda dataframe from artifact")
    df = pd.read_csv(artifact_local_path)

    logger.info("Remove outliers")
    idx = df['price'].between(float(args.min_price), float(args.max_price))
    df = df[idx].copy()

    logger.info("Convert last_review to datetime")
    df['last_review'] = pd.to_datetime(df['last_review'])

    logger.info("Save result to local file")
    df.to_csv(args.output_artifact, index=False)

    logger.info("upload artifact in wandb")
    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(args.output_artifact)

    logger.info("Logging artifact")
    run.log_artifact(artifact)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This steps cleans the data")


    parser.add_argument(
        "--input_artifact",
        type=str,
        help="please insert input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="please insert output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="output type is required",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="output description",
        required=False
    )

    parser.add_argument(
        "--min_price",
        type=str,
        help="minimum daily price for rental",
        required=False
    )

    parser.add_argument(
        "--max_price",
        type=str,
        help="maximum daily price for rental",
        required=False
    )

    args = parser.parse_args()

    go(args)