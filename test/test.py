from elapsedTimerPy import elapsedTimer

timer = elapsedTimer.Timer()

timer.set_start()
tmp1 = [i for i in range(10000)]
timer.add_point("point1")
tmp2 = [i for i in range(10000)]
timer.set_end()
timer.print()
