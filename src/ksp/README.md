- Setup 
    - CKAN install
        - wget https://github.com/KSP-CKAN/CKAN/releases/download/v1.34.4/ckan_1.34.4_all.deb
        - sudo apt-get install ./ckan_1.34.4_all.deb 

    - Start CKAN
        - Install krpc mod
    - Start Game from CKAN

- Run time
    - ADD krpc server
    - Run program from terminal
        - Accept connection from inside game
    - run python program


https://forum.kerbalspaceprogram.com/topic/206075-how-to-falcon-9-style-booster-without-the-panic/

http://www.braeunig.us/space/orbmech.htm


- Extra

    Build docker container

    docker pull ghcr.io/krpc/buildenv:latest
    docker run -it ghcr.io/krpc/buildenv:latest

    mkdir ksp
    pushd ksp
    wget https://github.com/krpc/ksp-lib/raw/main/ksp/ksp-1.12.5.zip
    unzip ksp-1.12.5.zip
    popd
    git clone https://github.com/krpc/krpc.git
    cd krpc
    ln -s `pwd`/../ksp lib/ksp
    ln -s /usr/lib/mono/4.5 lib/mono-4.5
    bazel build //...
    bazel test //:test

    bazel build //client/python:python


Server Mod - https://spacedock.info/mod/69/kRPC


- 
https://github.com/KSP-CKAN/CKAN

wget https://github.com/KSP-CKAN/CKAN/releases/download/v1.34.4/ckan_1.34.4_all.deb

sudo apt-get install ./ckan_1.34.4_all.deb 


https://krpc.github.io/krpc/getting-started.html#installation