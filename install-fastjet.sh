#!/bin/bash

prefix=${PWD}/fastjet
fastjet_version=3.3.0
fjcontrib_version=1.029

mkdir -p $prefix/src
cd $prefix/src

if [ ! -d fastjet-${fastjet_version} ]; then
    wget http://fastjet.fr/repo/fastjet-${fastjet_version}.tar.gz
    tar xfz fastjet-${fastjet_version}.tar.gz
fi

if [ ! -d fjcontrib-${fjcontrib_version} ]; then
    wget http://fastjet.hepforge.org/contrib/downloads/fjcontrib-${fjcontrib_version}.tar.gz
    tar xfz fjcontrib-${fjcontrib_version}.tar.gz
fi

cd fastjet-${fastjet_version}
./configure --prefix=$prefix --enable-allcxxplugins --enable-all-plugins
make -j8
make install
cd ../fjcontrib-${fjcontrib_version}
./configure --prefix=$prefix --fastjet-config=$prefix/bin/fastjet-config
make -j8
make install
make fragile-shared-install
 

