### I don't have ncs suggestions in vs code!

1. Type `alias` to preview where `venv-main` points to.
```
(main) expert@expert-cws:~$ alias | grep main
alias venv-main='echo "Activating main Python venv" && source ${HOME}/venvs/main/bin/activate'
```

2. Create symlinks between your NSO installation dir and site-packages inside main venv.
```
(main) expert@expert-cws:~$ ln -s ~/local-nso/src/ncs/pyapi/* ~/venvs/main/lib/python3.9/site-packages/.
```

3. Open python shell and verify the result
```
(main) expert@expert-cws:~$ python
Python 3.9.10 (main, Jan 15 2022, 18:17:56) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ncs
>>> ncs.__file__
'/home/expert/venvs/main/lib/python3.9/site-packages/ncs/__init__.py'
>>>
```

As you can see, ncs can be imported and it points to `/home/expert/venvs/main/lib/python3.9/site-packages/ncs/__init__.py`. You can verify how symlinks looks like in site-packages dir.
```
(main) expert@expert-cws:~$ ll /home/expert/venvs/main/lib/python3.9/site-packages/ | grep ^l
lrwxrwxrwx   1 expert expert       45 Feb  3 08:09 build.py -> /home/expert/local-nso/src/ncs/pyapi/build.py
lrwxrwxrwx   1 expert expert       40 Feb  3 08:09 doc -> /home/expert/local-nso/src/ncs/pyapi/doc/
lrwxrwxrwx   1 expert expert       41 Feb  3 08:09 ebin -> /home/expert/local-nso/src/ncs/pyapi/ebin/
lrwxrwxrwx   1 expert expert       53 Feb  3 08:09 gen-constants.py -> /home/expert/local-nso/src/ncs/pyapi/gen-constants.py
lrwxrwxrwx   1 expert expert       44 Feb  3 08:09 include -> /home/expert/local-nso/src/ncs/pyapi/include/
lrwxrwxrwx   1 expert expert       45 Feb  3 08:09 Makefile -> /home/expert/local-nso/src/ncs/pyapi/Makefile
lrwxrwxrwx   1 expert expert       48 Feb  3 08:09 MANIFEST.in -> /home/expert/local-nso/src/ncs/pyapi/MANIFEST.in
lrwxrwxrwx   1 expert expert       41 Feb  3 08:09 _ncs -> /home/expert/local-nso/src/ncs/pyapi/_ncs/
lrwxrwxrwx   1 expert expert       40 Feb  3 08:09 ncs -> /home/expert/local-nso/src/ncs/pyapi/ncs/
lrwxrwxrwx   1 expert expert       45 Feb  3 08:09 ncs_pyvm -> /home/expert/local-nso/src/ncs/pyapi/ncs_pyvm/
lrwxrwxrwx   1 expert expert       42 Feb  3 08:09 pysrc -> /home/expert/local-nso/src/ncs/pyapi/pysrc/
lrwxrwxrwx   1 expert expert       48 Feb  3 08:09 README.dist -> /home/expert/local-nso/src/ncs/pyapi/README.dist
lrwxrwxrwx   1 expert expert       40 Feb  3 08:09 src -> /home/expert/local-nso/src/ncs/pyapi/src/
lrwxrwxrwx   1 expert expert       44 Feb  3 08:09 tmp_fxs -> /home/expert/local-nso/src/ncs/pyapi/tmp_fxs/
lrwxrwxrwx   1 expert expert       44 Feb  3 08:09 VERSION -> /home/expert/local-nso/src/ncs/pyapi/VERSION
```

When you do `import ncs`, python uses "ncs" in site-packages, but since this is a symlink, the real file read is the one under your nso dir.

5. Restart VS Code and verify if code suggestion works now.
