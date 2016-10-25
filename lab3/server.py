#!/usr/bin/env python

import BookDatabase
import Pyro4.core
import Pyro4.naming


class remoteLibrary(Pyro4.core.ObjBase, BookDatabase.BookDatabase):
    def __init__(self, name):
        Pyro4.core.ObjBase.__init__(self)
        BookDatabase.BookDatabase.__init__(self, name)


def main():
    bd = remoteLibrary("mylib")
    Pyro4.core.initServer()

    locator = Pyro4.naming.NameServerLocator()
    ns = locator.getNS()
    print ns
    try:
        ns.createGroup(':libraries')
    except:
        pass
    daemon = Pyro4.core.Daemon()
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