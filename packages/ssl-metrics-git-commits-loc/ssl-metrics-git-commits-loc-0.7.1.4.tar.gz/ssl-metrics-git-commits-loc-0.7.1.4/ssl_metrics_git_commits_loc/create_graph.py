from argparse import ArgumentParser, Namespace
from operator import itemgetter
from os import path

import matplotlib.pyplot as plt
import numpy as np
import pandas
from matplotlib.figure import Figure
from pandas import DataFrame
from sklearn.metrics import r2_score


def getArgparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="Convert Output",
        usage="This program converts a JSON file into various different formats.",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The input data file that will be read to create the graphs",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-l",
        "--graph-loc-filename",
        help="The filename to output the LOC graph to",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-d",
        "--graph-delta-loc-filename",
        help="The filename to output the Delta LOC graph to",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-k",
        "--graph-k-loc-filename",
        help="The filename to output the K LOC graph to",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-m",
        "--maximum-degree-polynomial",
        help="Estimated maximum degree of polynomial",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-r",
        "--repository-name",
        help="Name of the repository that is being analyzed",
        type=str,
        required=False,
        default="",
    )
    return parser.parse_args()


def __findBestFitLine(x: list, y: list, maximumDegrees: int) -> tuple:
    # https://www.w3schools.com/Python/python_ml_polynomial_regression.asp
    data: list = []

    degree: int
    for degree in range(maximumDegrees):
        model: np.poly1d = np.poly1d(np.polyfit(x, y, degree))
        r2Score: np.float64 = r2_score(y, model(x))
        temp: tuple = (r2Score, model)
        data.append(temp)

    return max(data, key=itemgetter(0))


def _graphFigure(
    repositoryName: str,
    xLabel: str,
    yLabel: str,
    title: str,
    x: list,
    y: list,
    maximumDegree: int,
    filename: str,
) -> None:
    figure: Figure = plt.figure()
    plt.suptitle(repositoryName)

    # Actual Data
    plt.subplot(2, 2, 1)
    plt.xlabel(xlabel=xLabel)
    plt.ylabel(ylabel=yLabel)
    plt.title(title)
    plt.plot(x, y)
    plt.tight_layout()

    # Best Fit
    plt.subplot(2, 2, 2)
    data: tuple = __findBestFitLine(x=x, y=y, maximumDegrees=maximumDegree)
    bfModel: np.poly1d = data[1]
    line: np.ndarray = np.linspace(0, max(x), 100)
    plt.ylabel(ylabel=yLabel)
    plt.xlabel(xlabel=xLabel)
    plt.title("Best Fit Line")
    plt.plot(line, bfModel(line))
    plt.tight_layout()

    # Velocity of Best Fit
    plt.subplot(2, 2, 3)
    velocityModel = np.polyder(p=bfModel, m=1)
    line: np.ndarray = np.linspace(0, max(x), 100)
    plt.ylabel(ylabel="Velocity Unit")
    plt.xlabel(xlabel=xLabel)
    plt.title("Velocity")
    plt.plot(line, velocityModel(line))
    plt.tight_layout()

    # Acceleration of Best Fit
    plt.subplot(2, 2, 4)
    accelerationModel = np.polyder(p=bfModel, m=2)
    line: np.ndarray = np.linspace(0, max(x), 100)
    plt.ylabel(ylabel="Acceleration Unit")
    plt.xlabel(xlabel=xLabel)
    plt.title("Acceleration")
    plt.plot(line, accelerationModel(line))
    plt.tight_layout()

    figure.savefig(filename)
    figure.clf()


def plotLOC(
    df: DataFrame,
    xLabel: str,
    yLabel: str,
    title: str,
    maximumDegree: int,
    repositoryName: str,
    filename: str,
) -> tuple:
    x: list = [x for x in range(len(df["loc_sum"]))]
    y: list = df["loc_sum"].tolist()
    _graphFigure(
        repositoryName=repositoryName,
        xLabel=xLabel,
        yLabel=yLabel,
        title=title,
        x=x,
        y=y,
        maximumDegree=maximumDegree,
        filename=filename,
    )
    return (x, y)


def plotDeltaLOC(
    df: DataFrame,
    xLabel: str,
    yLabel: str,
    title: str,
    maximumDegree: int,
    repositoryName: str,
    filename: str,
) -> tuple:
    x: list = [x for x in range(len(df["delta_loc"]))]
    y: list = df["delta_loc"].tolist()
    _graphFigure(
        repositoryName=repositoryName,
        xLabel=xLabel,
        yLabel=yLabel,
        title=title,
        x=x,
        y=y,
        maximumDegree=maximumDegree,
        filename=filename,
    )
    return (x, y)


def plotKLOC(
    df: DataFrame,
    xLabel: str,
    yLabel: str,
    title: str,
    maximumDegree: int,
    repositoryName: str,
    filename: str,
) -> tuple:
    x: list = [x for x in range(len(df["kloc"]))]
    y: list = df["kloc"].to_list()
    _graphFigure(
        repositoryName=repositoryName,
        xLabel=xLabel,
        yLabel=yLabel,
        title=title,
        x=x,
        y=y,
        maximumDegree=maximumDegree,
        filename=filename,
    )
    return (x, y)


def main() -> None:
    locXLabel: str = "Commit"
    locYLabel: str = "LOC"
    locTitle: str = "Lines of Code (LOC) / Commits"

    dlocXLabel: str = locXLabel
    dlocYLabel: str = "ΔLOC"
    dlocTitle: str = "Change of Lines of Code (ΔLOC) / Days"

    klocXLabel: str = locXLabel
    klocYLabel: str = "KLOC"
    klocTitle: str = "Thousands of Lines of Code (KLOC) / Days"

    args: Namespace = getArgparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    df: DataFrame = pandas.read_json(args.input)

    loc: tuple = plotLOC(
        df=df,
        xLabel=locXLabel,
        yLabel=locYLabel,
        title=locTitle,
        maximumDegree=args.maximum_degree_polynomial,
        repositoryName=args.repository_name,
        filename=args.graph_loc_filename,
    )

    dloc: tuple = plotDeltaLOC(
        df=df,
        xLabel=dlocXLabel,
        yLabel=dlocYLabel,
        title=dlocTitle,
        maximumDegree=args.maximum_degree_polynomial,
        repositoryName=args.repository_name,
        filename=args.graph_delta_loc_filename,
    )

    kloc: tuple = plotKLOC(
        df=df,
        xLabel=klocXLabel,
        yLabel=klocYLabel,
        title=klocTitle,
        maximumDegree=args.maximum_degree_polynomial,
        repositoryName=args.repository_name,
        filename=args.graph_k_loc_filename,
    )


if __name__ == "__main__":
    main()
