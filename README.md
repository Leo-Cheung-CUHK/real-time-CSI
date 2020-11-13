# RPNC Installation Instructions

Author: Lizhao You  
Date: 11 April 2016  

## Hardware
  * N210 is preferred (USRP2 should also be workable);  
  * Full-duplex daugtherboard (e.g., SBX/CBX/RFX2400) is required;  
  * GPSDO is recommended;  
  * A powerful PC is recommended;  

## Software

1. Install Ubuntu Linux

    * Our testbed runs 64-bit Ubuntu Linux, version [12.04.3 LTS](http://releases.ubuntu.com/12.04.3/). You are of course free to use other OS, but we will only support this version.

2. [UHD](http://code.ettus.com/redmine/ettus/projects/uhd/wiki)

    * Build UHD software from source is recommended. Follow the [Build Instructions](http://code.ettus.com/redmine/ettus/projects/uhd/wiki/UHD_Build).  
    * Version >= 003.008.001 is preferred;  
    * Ensure the driver version and the hardware images are compatible.  

3. [GNURadio](http://gnuradio.org/redmine/projects/gnuradio/wiki)

    * Build GNURadio from source is recommended. Follow the [Build Instructions](http://gnuradio.org/redmine/projects/gnuradio/wiki/UbuntuInstall).  
    * Version 3.7.x is required;  
    * A patch that fixs the bug in delay block may be needed (see the user manual or README);  

4. RPNC

    * RPNC is built on [RawOFDM](http://people.csail.mit.edu/szym/rawofdm/README.html), an open-source implementation of OFDM for GNURadio. We have made some changes to accomodate the three-user PNC scenario.

    * Command
    ```
    $ mkdir build    
    $ cd build    
    $ cmake ../    
    $ make    
    $ make install
    ```

    * You can add cmake option, -DCMAKE_INSTALL_PREFIX, to indicate the location you want to install.
    * Remember to import the library path to where you install the source codes.  

## How to Run

  PNC
  
  ```
  $ ./test_pnc_tunnel_beacon_endnode.py --rx-freq 2.185G --tx-freq 2.585G --rx-args addr=192.168.20.2 --tx-args addr=192.168.20.2 -s 512 --node A --tx-amplitude 0.05 -W 5e6 --pause 0.015
  ```
  ```
  $ ./test_pnc_tunnel_beacon_endnode.py --rx-freq 2.185G --tx-freq 2.585G --rx-args addr=192.168.20.2 --tx-args addr=192.168.20.2 -s 512 --node B --tx-amplitude 0.03 -W 5e6 --pause 0.015
  ```
  ```
  $ ./test_pnc_relay.py --tx-freq 2.185G --rx-freq 2.585G --tx-args addr=192.168.20.2 --rx-args addr=192.168.20.2 -s 512 --tx-amplitude 0.15 --beacon-num 200000 --beacon-pause 0.03 -W 5e6 --time
  ```

  Point to Point
  
  ```
  $ ./test_ofdm_tx_main.py -f 2.185G -s 512 --pause 0.02 -W 5e6 -N 60000 --time
  ```
  ```
  $ ./test_ofdm_rx_main.py -f 2.185G -s 512 -W 5e6
  ```

## Experience

  * We tested RPNC on N210+GPSDO+SBX;  
  * We used three PCs, each of which has Intel Core i7 3.4GHz and 32G RAM.  

## Contact
  You are welcome to send the source code relevent questions to us:  

  * Lizhao You:  yl013@ie.cuhk.edu.hk
  * Haoyuan Pan: ph014@ie.cuhk.edu.hk
  * Jiaxin Liang: lj015@ie.cuhk.edu.hk
  

  Before you ask, you are recommended to read the docs/ folder first.
