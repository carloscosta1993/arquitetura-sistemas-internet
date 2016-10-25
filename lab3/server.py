#!/usr/bin/env python

import BookDatabase
import Pyro.core
import Pyro.naming


class remoteLibrary(Pyro.core.ObjBase, BookDatabase.BookDatabase):
    def __init__(self, name):
        Pyro.core.ObjBase.__init__(self)
        BookDatabase.BookDatabase.__init__(self, name)


def main():
    bd = remoteLibrary("mylib")
    Pyro.core.initServer()

    locator = Pyro.naming.NameServerLocator()
    ns = locator.getNS()
    print ns
    try:
        ns.createGroup(':libraries')
    except:
        pass
    daemon = Pyro.core.Daemon()
    daemon.useNameServer(ns)

    try:
        daemon.connect(bd, ':libraries.mylib')
    except:
        pass

    try:
        daemon.requestLoop()
    finally:
        daemon.shutdown(True)


if __name__ == "__main__":
    main()