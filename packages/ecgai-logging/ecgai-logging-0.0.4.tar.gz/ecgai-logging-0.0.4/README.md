# ecgai-logging

Logging decorator for both sync and async functions. Logging is carried out at logging levels DEBUG and INFO.

INFO logs Module name, Method name, Variables, Returns, Elapsed time

DEBUG logs Module name, Method name, Variables, Returns, Elapsed time, Synchronous or Asynchronous function type,
Working directory, Start time, End time
All times recorded in UTC

Exceptions are logged if the exception is not handled in code or the exception is handled and raised. If the exception
is handled in code and not raised it is not logged by this decorator
