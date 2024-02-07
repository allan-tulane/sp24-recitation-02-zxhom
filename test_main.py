from main import *


def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650

  assert simple_work_calc(40, 3, 2) == 730
  assert simple_work_calc(50, 3, 2) == 881
  assert simple_work_calc(20, 2, 2) == 92


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300

  assert work_calc(10, 1, 2, lambda n: n * n * n) == 1134
  assert work_calc(20, 2, 2, lambda n: 1) == 31
  assert work_calc(15, 3, 2, lambda n: n * n) == 480


def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work

  # create work_fn1
  # create work_fn2
  work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n*n*n)
  work_fn2 = lambda n: work_calc(n, 4, 2, lambda n: n*n)
  results = compare_work(work_fn1, work_fn2)
  print_results(results)



test_compare_work()


def test_compare_span():
  span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)
  span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: math.log(n))
  results = compare_span(span_fn1, span_fn2)
  print_results(results)


test_compare_span()
