import utils
from models import Model

if __name__ == "__main__":

    data = utils.load_from_csv('./ml_pro/data/happiness.csv')

    X, y = utils.features_target(data, ['country','rank','score'], 'score')

    model = Model()

    model.grid_training(X, y)

