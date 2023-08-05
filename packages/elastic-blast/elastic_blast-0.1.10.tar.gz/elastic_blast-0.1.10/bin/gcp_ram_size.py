#!/usr/bin/env python3
#                           PUBLIC DOMAIN NOTICE
#              National Center for Biotechnology Information
#  
# This software is a "United States Government Work" under the
# terms of the United States Copyright Act.  It was written as part of
# the authors' official duties as United States Government employees and
# thus cannot be copyrighted.  This software is freely available
# to the public for use.  The National Library of Medicine and the U.S.
# Government have not placed any restriction on its use or reproduction.
#   
# Although all reasonable efforts have been taken to ensure the accuracy
# and reliability of the software and data, the NLM and the U.S.
# Government do not and cannot warrant the performance or results that
# may be obtained by using this software or data.  The NLM and the U.S.
# Government disclaim all warranties, express or implied, including
# warranties of performance, merchantability or fitness for any particular
# purpose.
#   
# Please cite NCBI in any work or product based on this material.
"""
gcp_ram_size - helper utility reads machine type from stdin and prints RAM for the machine

Author: Victor Joukov joukovv@ncbi.nlm.nih.gov
"""
import sys
from elastic_blast.gcp_traits import get_machine_properties

if __name__ == "__main__":
    machineType = sys.stdin.read()
    props = get_machine_properties(machineType)
    print(props.memory)
    sys.exit(0)
