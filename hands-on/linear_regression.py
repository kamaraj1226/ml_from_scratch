"""
Linear regresssion
"""

from typing import List, Tuple
from plot import Plot

# features
# x1, x2
# [[x11, x12],
#  [x21, x22],
#  [x31, x32]
# ]
# result y looks like [0, 1, 2, 3]


class Feature:
    """
    Feature class to handle features
    """

    def __init__(self, *features: List[List[int | float]]) -> None:
        self.features = self.create_features(*features)
        self.row, self.col, _ = self.get_row_and_col()
        # negative one because adding x0 as 1 while creating
        self.shape = f"Row:{self.row} Column:{self.col-1}"

    def __str__(self) -> str:
        return f"{self.features}"

    def get_row_and_col(self) -> Tuple[int, int, int]:
        """
        Print shape of the features
        """
        return (
            len(self.features),
            len(self.features[0]) if len(self.features) > 0 else 0,
            0,
        )

    def create_features(
        self,
        *features: List[List[int | float]],
    ) -> Tuple[Tuple[int | float]]:
        """
        Given features return a matrix of features
        """
        matrix = ()
        x0_values = [1] * len(features[0])
        try:
            matrix = tuple(zip(x0_values, *features, strict=True))
        except ValueError as err:
            raise ValueError("Freatures are not in same size") from err

        return matrix


class LinearRegression(Plot):
    """
    Linear Regression
    """

    def __init__(
        self,
        features: Tuple[Tuple[int | float]],
        y_values: List[int],
        plot: bool = False,
    ) -> None:
        self.plot = plot
        if self.plot:
            super().__init__()

        self.features: Feature = features
        self.y_values = y_values

        self.__alpha = 0.0002  # learning rate
        # self.weights = [0] * (self.features.col)
        self.weights = [0] + [1] * (self.features.col - 1)

    def predict_y(self, feature):
        """
        build hypothesis function
        """
        total = 0
        for w, x in zip(self.weights, feature):
            total += w * x
        return total

    def cost(self):
        """
        Estimate cost
        Method: Mean Squre Error
        """
        error = 0
        for feature, y in zip(self.features.features, self.y_values):
            predicted_y = self.predict_y(feature)
            error += (predicted_y - y) ** 2
        error /= 2 * self.features.row
        return error

    def update_weights(self, new_weights):
        """
        Update weights
        """
        self.weights = new_weights

    def gradient_descent(self):
        """
        Tell me which direction i should move to find global minima
        """
        errors = []
        new_weights = []
        for i, w in enumerate(self.weights):
            error = 0
            for feature, y in zip(self.features.features, self.y_values):
                predicted_y = self.predict_y(feature)
                error += (predicted_y - y) * feature[i]
            error /= self.features.row
            errors.append(error)
            new_weights.append(w - (self.alpha * error))

        self.update_weights(new_weights)
        # print("Costs:", errors)

        if self.plot:
            self.plot_2d(errors, self.weights)

    def train(self, epoch):
        """
        Train model
        """
        print(f"Error before traning: {self.cost()}")
        for _ in range(epoch):
            self.gradient_descent()
            # print(f"Training {i+1}: Error:{self.cost()}")
        print(f"After Training: {self.cost()}")

    @property
    def alpha(self):
        """
        return learning rate
        """
        return self.__alpha

    @alpha.setter
    def alpha(self, new_alpha):
        if not isinstance(new_alpha, int) and not isinstance(new_alpha, float):
            raise ValueError(
                "Learning Rate value is not supported expected integer or float value."
            )
        self.__alpha = new_alpha

    def __str__(self) -> str:
        return f"Learning Rate: {self.alpha}\
            \nFeatures:{self.features.shape}\
            \nWeights: {self.weights}"


def main():
    """
    Main
    """
    # after getting value storing it in tuple will be easy to handle
    x1_values = [60, 67, 71, 75, 78]
    x2_values = [22, 24, 15, 20, 16]
    y_values = [140, 159, 192, 200, 212]

    try:
        f = Feature(x1_values, x2_values)
        l = LinearRegression(f, y_values=y_values)
        l.train(700)
        print(f"Weights: {l.weights}")

    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
