
import subprocess
import os
import time

SC_CMD="/usr/sbin/screencapture"
SC_OPT="-T1"
SC_DIR=os.path.dirname(__file__) + "/../sukusyo"
FILENAME_FORMAT="%Y%m%d%H%M%S.png"

def sc():
    filename = time.strftime(FILENAME_FORMAT, time.localtime())
    subprocess.call([SC_CMD, SC_OPT, "%s/%s" % (SC_DIR, filename)])

class CallbackModule(object):
    """
    makes Ansible much more evidencing on OS X.
    """
    def __init__(self):
        # plugin disable itself if screencapture is not present
        # ansible will not call any callback if disabled is set to True
        if not os.path.exists(SC_CMD):
            self.disabled = True
            print "%s does not exist, plugin %s disabled" % \
                    (SC_CMD, os.path.basename(__file__))
        else:
            if not os.path.exists(SC_DIR):
                os.makedirs(SC_DIR)

    def on_any(self, *args, **kwargs):
        pass

    def runner_on_failed(self, host, res, ignore_errors=False):
        sc()

    def runner_on_ok(self, host, res):
        sc()

    def runner_on_skipped(self, host, item=None):
        sc()

    def runner_on_unreachable(self, host, res):
        sc()

    def runner_on_no_hosts(self):
        pass

    def runner_on_async_poll(self, host, res, jid, clock):
        pass

    def runner_on_async_ok(self, host, res, jid):
        sc()

    def runner_on_async_failed(self, host, res, jid):
        sc()

    def playbook_on_start(self):
        sc()

    def playbook_on_notify(self, host, handler):
        sc()

    def playbook_on_no_hosts_matched(self):
        pass

    def playbook_on_no_hosts_remaining(self):
        pass

    def playbook_on_task_start(self, name, is_conditional):
        if not is_conditional:
            sc()
        else:
            sc()

    def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
        pass

    def playbook_on_setup(self):
        sc()

    def playbook_on_import_for_host(self, host, imported_file):
        pass

    def playbook_on_not_import_for_host(self, host, missing_file):
        pass

    def playbook_on_play_start(self, name):
        sc()

    def playbook_on_stats(self, stats):
        sc()

