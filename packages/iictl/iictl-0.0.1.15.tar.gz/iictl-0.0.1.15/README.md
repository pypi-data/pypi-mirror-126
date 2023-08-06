# iictl
cli를 통해 IntegratedInstance, pvc 등의 객체를 쉽게 생성/삭제하고 kubectl exec, kubectl cp를 binding하여 IntegratedInstance를 통해 접근 가능하도록 한다.

## kubernetes 인증

`login.kube.deep.est.ai`에 접속하여 회사 계정으로 google 로그인을 하면 config를 저장할 수 있는 스크립트 (mac, linux)가 출력된다. 그대로 복사하여 shell에 붙여넣기 하면 된다.

만약 directory가 없다는 오류가 나올 경우 `mkdir ~/.kube`를 실행한 뒤 다시 붙여넣기 한다.

## 설치

```
pip install iictl
```

## 사용

```
iictl [commands, options, ...]
```

linux에서는 root로 설치시 iictl이 root path에 등록되지만 나머지의 경우에 그렇지 않아서 path에 추가해 주어야 한다.

리눅스나 다음과 같은 명령어를 실행하면 path에 추가할 수 있다.

```
bash의 경우
echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc


zsh의 경우
echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.zshrc
source ~/.zshrc
```

path에 추가하지 않을 경우 다음과 같이 사용해야 한다.

```
python -m iictl [commands, options, ...]
```

## 쉘 자동완성

```
bash의 경우
echo 'eval "$(_IICTL_COMPLETE=bash_source iictl)"' >> ~/.bashrc

zsh의 경우
echo 'eval "$(_IICTL_COMPLETE=zsh_source iictl)"' >> ~/.zshrc
```

## instance

### create instance
```iictl run [options] 도커_이미지_이름 [커맨드]```

또는

```iictl run [options] 도커_이미지_이름 [-- 커맨드]```

도커 이미지 이름 뒤에도 옵션을 입력할 수 있다는 장점이 있다.

#### 옵션

|옵션|타입|설명|
|---|---|---|
|--name|str|이름을 지정할 수 있다. ~~지정하지 않을 경우 랜덤한 이름이 생성된다.~~|
|-e --env|str|key=value 형태의 environment variable. 여러번 사용이 가능하다.|
|-v --volume|str|volume:path 형태의 volume map. 여러번 사용이 가능하다.|
|--domain|str|port:domain 형태의 도메인 지정. domain은 *.kube.deep.est.ai 형태로 가능하다. 여러번 사용이 가능하다.|
|-w --workdir|str|container의 working dir 지정|
|--image-pull-secret|str|container registry 인증 정보 (아래 registry 참고)|
|--gpus|int|gpu 개수|
|--cpus|str|cpu limit 정수로 입력시 cpu 코어수, 100m와 같이 밀리코어수로 입력 가능하다|
|--gpu-node|rtx2080ti\|rtx3090|gpu 종류|

예시

```
iictl run --gpus=4 --cpus=20 --gpu-node=rtx2080ti --name=notebook -v notebook:/data -e TYPE=lab --domain 80:notebook.kube.deep.est.ai --workdir=/data caffeinism/pytorch-notebook -- jupyter blah blah ...
```

### delete instance
```iictl rm 인스턴스_이름```

```
iictl rm hello notebook ubuntu
```

### list instances
```iictl ps```

다음과 같은 형태로 출력된다.

```
name    image              status
------  -----------------  --------
hello   tutum/hello-world  Available
temp    busybox            Available
test    tutum/hello-world  Available
ubuntu  ubuntu             Available
```

### execute command in instance
```iictl exec [options] 인스턴스_이름 커맨드```

또는

```iictl exec [options] 인스턴스_이름 -- 커맨드```

|옵션|타입|설명|
|---|---|---|
|-t --tty|flag|TTY를 사용한다.|
|-i --stdin|flag|stdin을 사용한다.|

예시
```
iictl exec -it notebook -- bash
```

### view instance logs
```iictl logs [options] 인스턴스_이름```

|옵션|타입|설명|
|---|---|---|
|--tail|int|로그의 아래 tail줄만 출력한다.|
|-f --follow|flag|로그를 전부 출력하고 대기상태가 되며 이후 실행되어 추가된 로그도 계속 출력한다|

```
iictl logs --tail=100 -f notebook
```

### attach to instance
```iictl attach [options] 인스턴스_이름```

|옵션|타입|설명|
|---|---|---|
|-t --tty|flag|TTY를 사용한다.|
|-i --stdin|flag|stdin을 사용한다.|

예시
```
iictl attach -it notebook
```

### copy file to/from instance
```iictl cp 인스턴스_이름:/path localpath```

```iictl cp localpath 인스턴스_이름E:/path```

예시
```
iictl cp ./config/mygoodconfig.json notebook:/data/config
```

## volume

### create volume

```iictl volume create 볼륨_이름 볼륨_크기```

정수로 입력시 볼륨 크기의 기본 단위는 byte이다.

|사용 가능 단위|
|-------------|
|Mi|
|Gi|
|Ti|

### delete volume

```iictl volume rm 볼륨_이름```

### list volume

```iictl volume ls```

### protect & unprotect volume
실수로 volume rm을 통해 volume을 삭제하지 않도록 한다.

```iictl volume protect 볼륨_이름```

```iictl volume unprotect 볼륨_이름```

## resource
```iictl resources```

현재는 할당된 gpu의 양을 볼 수 있다.
```
$ iictl resources
node                 allocatable gpu
-----------------  -----------------
common-04-deepest                  0
common-05-deepest                  0
common-06-deepest                  0
common-07-deepest                  8
common-08-deepest                  0
common-09-deepest                  2
common-10-deepest                  0
```

## container registry

### save registry auth info
```iictl registry auth --from-cli```
```iictl registry auth --from-file 도커_인증_파일``` 

|옵션|타입|설명|
|---|---|---|
|--from-cli|flag|cli에서 registry 주소, username과 password를 입력하여 저장한다.|
|--from-file|str|인증 파일로부터 불러들인다. (기본적으로 도커에서는 ~/.docker/config.json에 저장된다)|

auth명령은 --from-cli나 --from-file 둘 중 **하나만** 지정해서 넣어야한다.

서버에 인증정보가 저장되는 것이기 떄문에 회사 계정 등의 공공적인 계정만 사용할것이 권장된다.

### list stored registry
현재 저장되어있는 인증정보의 이름을 출력한다.

```
$ iictl registry ls

name
------------------
caffeinism
docker.deep.est.ai
```
### remove 
```
$ iictl registry rm 인증_이름
```

## config

### config set

기본 namespace 변경

```
iictl config set namespace 네임스페이스_이름
```

### config get

```
iictl config get namespace
```


## metric

### view gpu status
