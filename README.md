# flask-mysql-restfulapi-on-docker
Flask環境とMySQL環境をDocker化  
Flask環境でRESTfulAPIを利用可能。ORMはSQLAlchemyを利用  
※ 基本参考資料を参考にしながら作成したが、動かないので改良。動作確認済み(2021/08/17)  
※ 開発環境はUbuntu20.04(wsl2)

# dockerのバージョン
```
> docker --version
Docker version 20.10.8, build 3967b7d

> docker-compose --version
docker-compose version 1.26.0, build d4451659
```


# プログラム全体手順
## dockerコンテナの作成と起動
```
docker-compose build
docker-compose up -d
```
※ 一回作ってあったらDBのテーブルデータ？消さないとエラーになる
※ 再実施する場合はmysql_dataを削除すること

## apiのコンテナに入って作業します
```
> docker-compose exec api bash
```
```
> flask db init
> flask db migrate
> flask db upgrade
```


# 動作確認
```
$ curl -X POST http://localhost:5000/hoges   -H "Content-Type:application/json"   -d "{\"name\":\"hoge\",\"state\":\"hoge\"}"
{
    "state": "hoge",
    "id": 3,
    "name": "hoge",
    "updateTime": "2021-08-16T20:39:31",
    "createTime": "2021-08-16T20:39:31"
}
$ curl -X POST http://localhost:5000/hoges   -H "Content-Type:application/json"   -d "{\"name\":\"hoge2\",\"state\":\"hoge2\"}"
{
    "state": "hoge2",
    "id": 4,
    "name": "hoge2",
    "updateTime": "2021-08-16T20:40:03",
    "createTime": "2021-08-16T20:40:03"
}

$ curl -X PUT http://localhost:5000/hoges/4 \
  -H ">   -H "Content-Type:application/json" \
 "{\">   -d "{\"name\":\"hogehoge\"}"

$ curl http://localhost:5000/hoges/4
{
    "updateTime": "2021-08-16T20:43:00",
    "createTime": "2021-08-16T20:40:03",
    "name": "hogehoge",
    "id": 4,
    "state": "hoge2"
}

$ curl http://localhost:5000/hoges
{
  "items": [
    {
      "createTime": "2021-08-16T20:35:35",
      "id": 1,
      "name": "hoge",
      "state": "hoge",
      "updateTime": "2021-08-16T20:35:35"
    },
    {
      "createTime": "2021-08-16T20:36:48",
      "id": 2,
      "name": "hoge",
      "state": "hoge",
      "updateTime": "2021-08-16T20:36:48"
    },
    {
      "createTime": "2021-08-16T20:39:31",
      "id": 3,
      "name": "hoge",
      "state": "hoge",
      "updateTime": "2021-08-16T20:39:31"
    },
    {
      "createTime": "2021-08-16T20:40:03",
      "id": 4,
      "name": "hogehoge",
      "state": "hoge2",
      "updateTime": "2021-08-16T20:43:00"
    }
  ]
}
```
DBの中身を確認後

DELETE
```
$ curl -X DELETE http://localhost:5000/hoges/4
$ curl http://localhost:5000/hoges/4
{
    "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
}
```



以下は部分確認するために確認するコマンド
# MySQLのDockerコンテナが立ち上がるか確認
```
docker-compose build db
docker-compose up -d db
docker-compose exec db mysql -u root -p
mysql>
```

# FlaskのDockerコンテナが起動するか確認
```
docker-compose build api
docker-compose up -d api
docker-compose logs api
```

# docker-compose build db 時に ERROR: readlink /var/lib/docker/overlay2/l: invalid argumentが出る場合
```
service docker stop
sudo rm -rf /var/lib/docker
docker-compose down --rmi all --volumes --remove-orphans
sudo service docker start
```

# docker コンテナを一括消去するコマンド docker-compose down
```
docker-compose down --rmi all --volumes --remove-orphans
```

# dockerデーモン起動
```
$ sudo service docker start
```

# dockerデーモンステータス確認
```
$ sudo service docker status
```

# dockerデーモン停止
```
$ sudo service docker stop
```

# ログ確認
```
docker-compose logs
docker-compose logs db_1
```


# 参考資料：
> https://cloudpack.media/43980  
> https://qiita.com/K_ichi/items/e8826c300e797b90e40f  
> https://qiita.com/kai_kou/items/5d73de21818d1d582f00  
> https://stackoverflow.com/questions/44942790/docker-error-failed-to-register-layer-symlink  
> https://qiita.com/zono_0/items/7a25d283cd4b09d6ffb0  
> https://github.com/marshmallow-code/flask-marshmallow/issues/56  
