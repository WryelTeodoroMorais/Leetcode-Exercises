import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    l, c = players.shape

    result = [l, c]

    return result