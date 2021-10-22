import numpy as np
from scipy.spatial import distance
from Point import Point

class DBSCAN:
  """
  DBSCANアルゴリズム

  Attributes
  ----------
  eps : float
    ある点からの半径ε
  min_samples : int
    密領域を形成するために必要な点の最小数MinPts
  points : list of Point
    与えられた点集合のリスト
  label : int
    次に設定するクラスタの番号
  """
  def __init__(self, eps, min_samples):
    """
    Parameters
    ----------
    eps : float
      ある点からの半径ε
    min_samples : int
      密領域を形成するために必要な点の最小数MinPts
    """
    self.eps = eps
    self.min_samples = min_samples
    self.points = None
    self.label = 0

  def get_labels(self):
    """
    Returns
    ----------
    labels : list of int
      各点に付与されたクラスタ番号のリスト
    """
    return [p.label for p in self.points]

  def get_pointTypes(self):
    """
    Returns
    ----------
    pointTypes : list of str
      各点に付与されたpointTypeのリスト
    """
    return [p.pointType for p in self.points]
  
  def rangeQuery(self, p):
    """
    与えられた点のε近傍点を探索する．

    Parameters
    ----------
    p : Point
      探索する中心点

    Returns
    ----------
    neighborPoints : list of Point
      点pのε近傍点のリスト
    """
    return [q for q in self.points if distance.euclidean(p.x, q.x) <= self.eps]

  def expandCluster(self, p, neighborPts):
    """
    あるcore pointから到達可能な点をクラスタとして拡大する．

    Parameters
    ----------
    p : Point
      始点となるcore point
    neighborPts : list of Point
      点pのε近傍点
    """
    p.label = self.label
    for q in neighborPts:
      if not q.visited:
        q.visit()
        neighborPts_q = self.rangeQuery(q)
        if len(neighborPts_q) >= self.min_samples:
          q.pointType = "CORE"
          neighborPts.extend(neighborPts_q)
      if q.label == -1:
        q.label = self.label

  def fit(self, X):
    """
    クラスタリングを実行する．

    Parameters
    ----------
    X : list
      クラスタリングを実行するデータ
    """
    self.points = [Point(x) for x in X]
    for p in self.points:
      if not p.visited:
        p.visit()
        neighborPts = self.rangeQuery(p)
        if len(neighborPts) < self.min_samples:
          p.pointType = "NOISE"
        else:
          p.pointType = "CORE"
          self.expandCluster(p, neighborPts)
          self.label += 1
       
    