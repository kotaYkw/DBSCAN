class Point:
  """
  Pointクラス

  Attributes
  ----------
  x : list
    点の座標
  visited : bool, default=False
    点がスキャン済みかを示す真偽値
  pointType : str, default=''
    点の種類('CORE', 'NOISE'など)を示す文字列
  label : int, default=-1
    点の属するクラスタの番号．ノイズの場合は-1．
  """
  def __init__(self, x):
    self.x = x
    self.visited = False
    self.pointType = ''
    self.label = -1

  @property
  def x(self):
    return self.__x
    
  @x.setter
  def x(self, value):
    self.__x = value

  @property
  def visited(self):
    return self.__visited
    
  @visited.setter
  def visited(self, value):
    if not isinstance(value, bool):
      raise TypeError("visited must be an bool.")
    self.__visited = value

  @property
  def pointType(self):
    return self.__pointType

  @pointType.setter
  def pointType(self, value):
    if not isinstance(value, str):
      raise TypeError("pointType must be an string.")
    self.__pointType = value

  @property
  def label(self):
    return self.__label
  
  @label.setter
  def label(self, value):
    if not isinstance(value, int):
      raise TypeError("label must be an integer.")
    self.__label = value

  def visit(self):
    """
    この点をスキャンしたときに実行する．
    """
    self.visited = True