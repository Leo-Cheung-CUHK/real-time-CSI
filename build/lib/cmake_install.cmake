# Install script for directory: /home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/spiral/viterbi.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/spiral/parity.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_peak_detector_fb.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_peak_detector2_fb.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_message_sink.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_msg_queue.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_pnc_frequency_modulator_fc.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_message_source.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_regenerate_peak2.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_regenerate_peak3.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/util/raw_divide_ff.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/qam/raw_qam.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/qam/raw_conv.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/qam/raw_intrlv.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/qam/raw_scrambler_bb.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/raw" TYPE FILE FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_ofdm_mapper.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_ofdm_sampler.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_ofdm_cyclic_prefixer.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_ofdm_insert_preamble.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_ofdm_demod.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_pnc_demod.h"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/lib/ofdm/raw_ofdm_insert_amble.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librawofdm.so.1.3.7"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librawofdm.so.1.3"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librawofdm.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/lib/librawofdm.so.1.3.7"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/lib/librawofdm.so.1.3"
    "/home/lihao/Documents/SDR_Gnuradio/rpnc-release-7621b9ddcd85-gr3.7.x-54afffeca09e/build/lib/librawofdm.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librawofdm.so.1.3.7"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librawofdm.so.1.3"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librawofdm.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

