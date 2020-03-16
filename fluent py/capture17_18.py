"""
通常情况下自己不应该创造期物，只能由并发框架实例化，
因为期物表示终将发生的事情，而确定某件事会发生的唯一方式是执行的时间已经排定
因此只有排定把某件事交给concurrent.futures.Execute子类处理时才会创建future实例

cpython解释器本身不是线程安全的，因此有全局解释器锁（GIL），一次只允许使用一个线程执行字节码，因此不能同时使用多个cpu
执行阻塞型I/O操作的函数在等待操作系统返回结果时会释放GIL，因此I/O密集型能使用多线程，
在一个python线程等待网络响应时，阻塞型I/O函数会释放GIL再运行一个线程
"""