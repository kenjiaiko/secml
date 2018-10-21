This is a sample code using FFRI Dataset 2018 on MWS2018.
```
$ cp FFRIDataset2018/malware.csv ./malware.csv
$ cp FFRIDataset2018/cleanware.csv ./cleanware.csv
$ python csv2json.py malware.csv
$ python csv2json.py cleanware.csv
$ python detect_test.py 10 10
1.step: read ok
2.step: update ok
3.step: score ok
turn.1
7460 19682
3956 210000
turn.2
7430 19682
0 210000
$ python detect_test2.py 10 10
1.step: read ok
2.step: update ok
3.step: score ok
turn.1
9179 19682
13447 210000
turn.2
9128 19682
0 210000
```


```
$ python cuckoo2json.py MWS_dataset/FFRI_Dataset_2013/ ./ 2013
$ python cuckoo2json.py MWS_dataset/FFRI_Dataset_2014/Cuckoo/ ./ 2014
$ python cuckoo2json.py MWS_dataset/FFRI_Dataset_2015/FFRI_Dataset2015/ ./ 2015
$ python cuckoo2json.py MWS_dataset/FFRI_Dataset_2016/FFRIDataset2016/10/ ./ 2016
$ python cuckoo2json.py MWS_dataset/FFRI_Dataset_2017/FFRI\ Dataset\ 2017/ ./ 2017
```

```
$ python maketree.py 20 ./2013/
$ mv tree.pickle 2013.pickle
$ python maketree.py 20 ./2014/
$ mv tree.pickle 2014.pickle
$ python maketree.py 20 ./2015/
$ mv tree.pickle 2015.pickle
$ python maketree.py 20 ./2016/
$ mv tree.pickle 2016.pickle
$ python maketree.py 20 ./2017/
$ mv tree.pickle 2017.pickle
```

```
$ python checktree.py ./2013/ 2013 20 100
2248 2600 0.864615384615
$ python checktree.py ./2014/ 2014 20 100
2780 2900 0.958620689655
$ python checktree.py ./2015/ 2015 20 100
2363 3000 0.787666666667
$ python checktree.py ./2016/ 2016 20 100
7166 8200 0.873902439024
$ python checktree.py ./2017/ 2017 20 100
6166 6200 0.994516129032
```

```
$ python checktree2.py ./2014/ 2013 20 100 ./2013/
2447 2900 0.843793103448
$ python checktree2.py ./2015/ 2014 20 100 ./2014/
800 3000 0.266666666667
$ python checktree2.py ./2016/ 2015 20 100 ./2015/
2509 8200 0.305975609756
$ python checktree2.py ./2017/ 2016 20 100 ./2016/
4281 6200 0.690483870968
```
