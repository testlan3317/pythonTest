# Example 1 - logging to standard output for systemd
# when using systemd to run a daemon, applications can just send log messages to stdout or stderr and have systemd forward the messages to journald and syslog.
# An additional perk, this does not require catching exceptions, as python already writes those to standard error. 
# In the case of running Python in containers like Docker, logging to standard output is often the easiest move as this output can be directly and easily 
# managed by the container itself.

import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
exit(main())


# However, a potential problem with this solution is that exceptions are logged as multiple lines, which can cause problems for later analysis. 
# Sadly, configuring Python to send multi-line exceptions as a single line is often not quite as simple, but certainly possible.
# Note the implemention in "logging4.py", calling logging.exception is a shorthand equivalent to "logging.error(..., exc_info=True)."

