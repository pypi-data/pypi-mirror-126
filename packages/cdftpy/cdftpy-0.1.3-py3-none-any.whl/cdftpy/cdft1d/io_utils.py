#!/usr/bin/python
# -*- coding: utf-8 -*-
import ast
import os.path
import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np


def print_simulation(solute, solvent_model, params):

    print("Solute:")
    print("   {name} charge={charge} sigma={sigma} epsilon={eps}".format(**solute))
    print("Simulation parameters:")
    for k, v in params.items():
        print("  ", k, v)
    print(f"   solvent {solvent_model.filename}")
    print("Solvent model:")
    print(f"   name {solvent_model.aname}")
    print(f"   file  {solvent_model.filename}")
    print(f"   ngrid {solvent_model.ifft.ngrid}")
    print(f"   density {solvent_model.density}")
    print(f"   temp {solvent_model.temp}")


def print_banner(title):
    dash = "-" * len(title)
    print(dash)
    print(title)
    print(dash)


def iter_lines(fp):
    for line in fp:
        record = line.rsplit("#")[0].strip()
        if record == "":
            continue
        else:
            yield record


def read_key_value(filename, section):

    tag = f"<{section}>"

    params = {}

    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            return None
        for line in iter_lines(fp):
            if line.startswith("<"):
                break
            tokens = line.split()
            if len(tokens) == 2:
                key, value = tokens
                try:
                    value = ast.literal_eval(value)
                except ValueError:
                    pass
            elif len(tokens) == 1:
                key, value = tokens[0], True
            params[key] = value
        return params


def read_solute(filename, section="solute"):

    name_list = []
    sigma_list = []
    eps_list = []
    charge_list = []
    x_list = []
    y_list = []
    z_list = []

    tag = f"<{section}>"
    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            print(f"cannot find {tag} section")
            sys.exit(1)
        for line in iter_lines(fp):
            if line.startswith("<"):
                break
            name, sigma, eps, charge, *xyz = line.split()
            name_list.append(name)
            sigma_list.append(float(sigma))
            eps_list.append(float(eps))
            charge_list.append(float(charge))
            if len(xyz) < 3:
                xyz = [0] * 3
            x_list.append(float(xyz[0]))
            y_list.append(float(xyz[1]))
            z_list.append(float(xyz[2]))

    return dict(
        name=np.array(name_list),
        sigma=np.array(sigma_list),
        eps=np.array(eps_list),
        charge=np.array(charge_list),
        x=np.array(x_list),
        y=np.array(y_list),
        z=np.array(z_list),
    )


def read_geom(filename, section="geometry"):

    name_list = []
    atype_list = []
    x_list = []
    y_list = []
    z_list = []

    tag = f"<{section}>"
    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            print(f"cannot find {tag} section")
            sys.exit(1)
        for line in iter_lines(fp):
            if line.startswith("<"):
                break
            name, atype, x, y, z = line.split()
            name_list.append(name)
            atype_list.append(atype)
            x_list.append(float(x))
            y_list.append(float(y))
            z_list.append(float(z))

    return dict(
        aname=np.array(name_list),
        atype=np.array(atype_list),
        x=np.array(x_list),
        y=np.array(y_list),
        z=np.array(z_list),
    )


def read_interaction(filename, section="interactions"):

    ff = dict()
    tag = f"<{section}>"
    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            print(f"cannot find {tag} section")
            sys.exit(1)
        for line in iter_lines(fp):
            if line.startswith("<"):
                break
            name, sigma, eps, charge = line.split()
            ff[name] = dict(sigma=float(sigma), eps=float(eps), charge=float(charge))

    return ff


def read_rism_patch(filename, section="rism_patch"):

    ff = dict()
    tag = f"<{section}>"
    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            print(f"cannot find {tag} section")
            return ff
        for line in iter_lines(fp):
            if line.startswith("<"):
                break
            name, sigma, eps = line.split()
            ff[name] = dict(sigma=float(sigma), eps=float(eps))

    return ff


def read_system(
    filename,
    geometry_section="geometry",
    interaction_section="interactions",
    rism_patch=False,
):

    sigma_list = []
    eps_list = []
    charge_list = []

    system = read_geom(filename, section=geometry_section)
    ff = read_interaction(filename, interaction_section)

    for i, name in enumerate(system["atype"]):
        sigma_list.append(ff[name]["sigma"])
        eps_list.append(ff[name]["eps"])
        charge_list.append(ff[name]["charge"])

    if rism_patch:
        ff_rism = read_rism_patch(filename)
        for i, name in enumerate(system["atype"]):
            if name in ff_rism:
                print("found", ff_rism[name])
                sigma_list[i] = ff_rism[name]["sigma"]
                eps_list[i] = ff_rism[name]["eps"]

    system["sigma"] = np.array(sigma_list)
    system["eps"] = np.array(eps_list)
    system["charge"] = np.array(charge_list)

    return system


def read_system_to_class(
    filename,
    geometry_section="geometry",
    interaction_section="interactions",
    rism_patch=False,
):

    sigma_list = []
    eps_list = []
    charge_list = []

    system = read_geom(filename, section=geometry_section)
    ff = read_interaction(filename, interaction_section)

    for i, name in enumerate(system["atype"]):
        sigma_list.append(ff[name]["sigma"])
        eps_list.append(ff[name]["eps"])
        charge_list.append(ff[name]["charge"])

    if rism_patch:
        ff_rism = read_rism_patch(filename)
        for i, name in enumerate(system["atype"]):
            if name in ff_rism:
                print("found", ff_rism[name])
                sigma_list[i] = ff_rism[name]["sigma"]
                eps_list[i] = ff_rism[name]["eps"]

    system["sigma"] = np.array(sigma_list)
    system["eps"] = np.array(eps_list)
    system["charge"] = np.array(charge_list)

    return system

def read_array(filename, section):

    tag = f"<{section}>"

    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            # print(f"cannot find {tag} section in {os.path.abspath(filename)}")
            return None, None
        line = fp.readline()
        nv,ngrid= map(int, line.split())
        kgrid = np.zeros(shape=ngrid)
        a_k = np.zeros(shape=(nv, nv, ngrid), dtype=np.double)

        for ig, line in enumerate(iter_lines(fp)):
            if line.startswith("<"):
                break
            row = list(map(float, line.split()))
            kgrid[ig] = row[0]
            n = 1
            for i in range(nv):
                for j in range(i, nv):
                    a_k[i, j, ig] = row[n]
                    a_k[j, i, ig] = row[n]
                    n = n + 1

        return a_k, kgrid

def read_array_old(nv, ngrid, filename, section):

    tag = f"<{section}>"

    with open(filename, "r") as fp:
        if find_section(tag, fp) is None:
            # print(f"cannot find {tag} section in {os.path.abspath(filename)}")
            return None, None
        ngrid = int(fp.readline())
        kgrid = np.zeros(shape=ngrid)
        a_k = np.zeros(shape=(nv, nv, ngrid), dtype=np.double)

        for ig, line in enumerate(iter_lines(fp)):
            if line.startswith("<"):
                break
            row = list(map(float, line.split()))
            kgrid[ig] = row[0]
            n = 1
            for i in range(nv):
                for j in range(i, nv):
                    a_k[i, j, ig] = row[n]
                    a_k[j, i, ig] = row[n]
                    n = n + 1

        return a_k, kgrid
def array_read(nv, ngrid, filename):

    with open(filename, "r") as fp:
        grid = np.zeros(shape=ngrid)
        s_k = np.zeros(shape=(nv, ngrid), dtype=np.double)

        for ig, line in enumerate(iter_lines(fp)):
            row = list(map(float, line.split()))
            grid[ig] = row[0]
            n = 1
            for i in range(nv):
                s_k[i, ig] = row[i + 1]

        return s_k


def find_section(section, fp):

    iline = None
    for i, line in enumerate(fp, 1):
        if line.strip() == section:
            iline = i
            break

    return iline


if __name__ == "__main__":
    filename = "/Users/marat/codes/cdft-dev/data/input.dat"
    print(read_solute(filename))
