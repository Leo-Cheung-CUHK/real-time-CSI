# Copyright 2010-2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# This file included, use CMake directory variables
########################################################################
set(tmp_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_mapper.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_sampler.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_cyclic_prefixer.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_insert_preamble.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_demod.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_pnc_demod.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_insert_amble.cc
)

########################################################################
# Setup sources and includes
########################################################################
list(APPEND rawofdm_sources ${tmp_sources})

install( FILES 
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_mapper.h
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_sampler.h
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_cyclic_prefixer.h
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_insert_preamble.h
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_demod.h
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_pnc_demod.h
    ${CMAKE_CURRENT_SOURCE_DIR}/raw_ofdm_insert_amble.h
    DESTINATION ${GR_INCLUDE_DIR}/raw
)

