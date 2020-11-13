export RPNC_INSTALL_DIR=/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/install
export PYTHONPATH=$PYTHONPATH:$RPNC_INSTALL_DIR/lib/python2.7/dist-packages
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RPNC_INSTALL_DIR/lib
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:$RPNC_INSTALL_DIR/lib/pkgconfig

sudo sysctl -w net.core.wmem_max=1048576
sudo sysctl -w net.core.rmem_max=50000000
