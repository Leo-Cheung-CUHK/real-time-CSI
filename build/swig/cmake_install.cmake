# Install script for directory: /home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/swig

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE MODULE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/_raw_ofdm.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so"
         OLD_RPATH "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_ofdm.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_ofdm.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_ofdm.pyc"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_ofdm.pyo"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE MODULE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/_raw_util.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so"
         OLD_RPATH "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_util.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_util.pyc"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_util.pyo"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE MODULE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/_raw_qam.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so"
         OLD_RPATH "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw/_raw_qam.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_qam.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_qam.pyc"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_qam.pyo"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/raw/swig" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/swig/raw_ofdm.i"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/swig/raw_util.i"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/swig/raw_qam.i"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_swig.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_swig.pyc"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/swig/raw_swig.pyo"
    )
endif()

