#!/usr/bin/env python3
"""Order matters.
"""
def StrumGuitar(measures):
    for measure in range(measures):
        print("strum. strum.")
    BeatDrum(measures)

StrumGuitar(2)

def BeatDrum(measures):
    for measure in range(measures):
        print("boom! boom!")
