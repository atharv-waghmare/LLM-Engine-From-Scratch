from data_pipeline.clustering import DSU

def test_dsu_():
  dsu = DSU(5)
  assert dsu.find(0) != dsu.find(1)

  dsu.union(0, 1)
  dsu.union(2, 3)

  assert dsu.find(0) == dsu.find(1)
  assert dsu.find(2) == dsu.find(3)

  dsu.union(1, 2)

  assert dsu.find(0) == dsu.find(3)

  assert dsu.find(4) != dsu.find(0)
