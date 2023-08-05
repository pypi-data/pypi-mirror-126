from nnmdkit.util import Util


class Lammps:
    '''nnmdkit.core.Lammps.Lammps

    Template object to contain LAMMPS initialization settings

    Attributes:
        data_fname: str
            File name of the data file, which will be read in by read_data command

        NN_POTENTIAL: str
            Neural network potential file name

        atom_style: str
            LAMMPS aomt_style to use during simulation; default=full

        units: str
            LAMMPS units to use during simulation; default=real

        timestep: float
            LAMMPS timestep to use during simulation; default=1 fs

        neighbor_skin: float
            LAMMPS neighbor skin size to use during simulation; default=2.0 Angstrom

        neighbor_every: int
            LAMMPS neighbor list checking frequency to use during simulation; default=1 fs

        thermo: int
            LAMMPS thermo to use during simulation; default=1000 timestep

        pair_style: str
            LAMMPS pair_style to use during simulation; default=nn

        element: str
            Element order of the pair_style; default=C H
    '''
    def __init__(self,
                 data_fname,
                 NN_POTENTIAL,
                 atom_style='full',
                 units='metal',
                 timestep=0.001,
                 neighbor_skin=2.0,
                 neighbor_every=1,
                 thermo=100,
                 pair_style='nn',
                 element='C H'):
        self.data_fname = data_fname
        self.NN_POTENTIAL = NN_POTENTIAL
        self.atom_style = atom_style
        self.units = units
        self.timestep = timestep
        self.neighbor_skin = neighbor_skin
        self.neighbor_every = neighbor_every
        self.thermo = thermo
        self.pair_style = pair_style
        self.element = element

    def add_procedure(self, procedure, **kwargs):

        # key = min_style, etol, ftol, maxiter, maxeval
        if procedure == 'minimization':
            self.min_kwargs = {
                'min_style': 'cg',
                'etol': 10**(-6),
                'ftol': 10**(-8),
                'maxiter': 10**5,
                'maxeval': 10**7
            }
            Util.register_kwargs(self.min_kwargs, kwargs)

        # key = Tfinal, Pfinal, Tmax, Pmax, Tdamp, Pdamp, eq_totaltime
        elif procedure == 'equilibration':

            self.eq_kwargs = {
                'eq_step': [],
                'Tfinal': 300,
                'Pfinal': 1,
                'Tmax': 1000,
                'Pmax': 50000,
                'Tdamp': '$(100.0*dt)',
                'Pdamp': '$(100.0*dt)',
                'eq_totaltime': 0
            }
            Util.register_kwargs(self.eq_kwargs, kwargs)

            # If equilibration steps are not defined, apply the default 21-step amorphous polymer equilibration process
            # Ref: Abbott, Hart, and Colina, Theoretical Chemistry Accounts, 132(3), 1-19, 2013.
            if self.eq_kwargs['eq_step'] == []:
                Tmax = self.eq_kwargs['Tmax']
                Tfinal = self.eq_kwargs['Tfinal']
                Pmax = self.eq_kwargs['Pmax']
                Pfinal = self.eq_kwargs['Pfinal']
                self.eq_kwargs['eq_step'] = [
                    ['nvt', 50000, Tmax],
                    ['nvt', 50000, Tfinal],
                    ['npt', 50000, Tfinal, 0.02 * Pmax],
                    ['nvt', 50000, Tmax],
                    ['nvt', 100000, Tfinal],
                    ['npt', 50000, Tfinal, 0.6 * Pmax],
                    ['nvt', 50000, Tmax],
                    ['nvt', 100000, Tfinal],
                    ['npt', 50000, Tfinal, Pmax],
                    ['nvt', 50000, Tmax],
                    ['nvt', 100000, Tfinal],
                    ['npt', 5000, Tfinal, 0.5 * Pmax],
                    ['nvt', 5000, Tmax],
                    ['nvt', 10000, Tfinal],
                    ['npt', 5000, Tfinal, 0.1 * Pmax],
                    ['nvt', 5000, Tmax],
                    ['nvt', 10000, Tfinal],
                    ['npt', 5000, Tfinal, 0.01 * Pmax],
                    ['nvt', 5000, Tmax],
                    ['nvt', 10000, Tfinal],
                    ['npt', 800000, Tfinal, Pfinal],
                ]

            for i in self.eq_kwargs['eq_step']:
                self.eq_kwargs['eq_totaltime'] += i[1]

        # key = Tinit, Tfinal, Tinterval, step, pressure, Pdamp, Tdamp
        elif procedure == 'Tg_measurement':
            self.Tg_kwargs = {
                'Tinit': 500,
                'Tfinal': 100,
                'Tinterval': 20,
                'step': 1000000,
                'pressure': 1,
                'Tdamp': '$(100.0*dt)',
                'Pdamp': '$(100.0*dt)'
            }
            Util.register_kwargs(self.Tg_kwargs, kwargs)

    def write_input(self, output_dir):

        Util.build_dir(output_dir)

        # Write settings file
        settings_fname = 'system.in.settings'
        with open(output_dir + '/' + settings_fname, 'w') as f:
            f.write('{:<15} {}\n'.format('pair_style', self.pair_style))
            f.write('{:<15} * * {} {}\n'.format('pair_coeff',
                                                self.NN_POTENTIAL,
                                                self.element))
            f.write('\n')
            f.write('{:<15} {} bin\n'.format('neighbor', self.neighbor_skin))
            f.write('{:<15} delay 0 every {} check yes\n'.format(
                'neigh_modify', self.neighbor_every))
            f.write('\n')
            f.write(
                '{:<15} custom step temp density vol press ke pe ebond evdwl ecoul elong\n'
                .format('thermo_style'))
            f.write('{:<15} {}\n'.format('thermo', self.thermo))
            f.write('{:<15} {}\n'.format('timestep', self.timestep))

        # Write LAMMPS input file
        lmp_input_fname = 'lmp.in'
        with open(output_dir + '/' + lmp_input_fname, 'w') as f:

            f.write('# LAMMPS input file generated by NNMDKit\n')
            f.write('\n')

            f.write('### Initialization\n')
            f.write('{:<15} full\n'.format('atom_style'))
            f.write('{:<15} real\n'.format('units'))
            f.write('{:<15} {}\n'.format('read_data', self.data_fname))
            f.write('{:<15} {}\n'.format('include', settings_fname))
            f.write('\n')
            f.write('\n')

            # If minimization is added to the lammps procedure
            if hasattr(self, 'min_kwargs'):
                f.write('### Minimization\n')
                f.write('{:<15} {}\n'.format('min_style',
                                             self.min_kwargs['min_style']))
                f.write('{:<15} {} {} {} {}\n'.format(
                    'minimize', self.min_kwargs['etol'],
                    self.min_kwargs['ftol'], self.min_kwargs['maxiter'],
                    self.min_kwargs['maxeval']))
                f.write('{:<15} 0\n'.format('reset_timestep'))
                f.write('\n')
                f.write('\n')

            # If equilibration is added to the lammps procedure
            if hasattr(self, 'eq_kwargs'):
                f.write('### Equilibration\n')
                f.write(
                    '{:<15} dump1 all custom 10000 equil.lammpstrj id mol type q xs ys zs ix iy iz\n'
                    .format('dump'))
                f.write('{:<15} {} equilibrated.restart\n'.format(
                    'restart', self.eq_kwargs['eq_totaltime']))
                f.write('\n')

                for n, i in enumerate(self.eq_kwargs['eq_step']):
                    if i[0] == 'nvt':
                        f.write('{:<15} step{} all nvt temp {} {} {}\n'.format(
                            'fix', n + 1, i[2], i[2], self.eq_kwargs['Tdamp']))
                    elif i[0] == 'npt':
                        f.write(
                            '{:<15} step{} all npt temp {} {} {} iso {} {} {}\n'
                            .format('fix', n + 1, i[2], i[2],
                                    self.eq_kwargs['Tdamp'], i[3], i[3],
                                    self.eq_kwargs['Pdamp']))
                    f.write('{:<15} {}\n'.format('run', i[1]))
                    f.write('{:<15} step{}\n'.format('unfix', n + 1))
                    f.write('\n')
                f.write('{:<15} dump1\n'.format('undump'))
                f.write('{:<15} 0\n'.format('reset_timestep'))
                f.write('\n')
                f.write('\n')

            # If equilibration is added to the lammps procedure
            if hasattr(self, 'Tg_kwargs'):
                step = self.Tg_kwargs['step']
                f.write('### Production - Tg measurement\n')
                f.write(
                    '{:<15} dump2 all custom 10000 production.lammpstrj id mol type q xs ys zs ix iy iz\n'
                    .format('dump'))
                f.write('{:<15} {} production.restart\n'.format(
                    'restart', step))
                f.write('{:<15} Rho equal density\n'.format('variable'))
                f.write('{:<15} Temp equal temp\n'.format('variable'))
                f.write(
                    '{:<15} fDENS all ave/time {} {} {} v_Temp v_Rho file temp_vs_density\n'
                    .format('fix', int(step / 100 / 4), 100, step))
                f.write('\n')

                f.write('{:<15} loop\n'.format('label'))
                f.write('{:<15} a loop {}\n'.format(
                    'variable',
                    int((self.Tg_kwargs['Tinit'] - self.Tg_kwargs['Tfinal']) /
                        self.Tg_kwargs['Tinterval'] + 1)))
                f.write('{:<15} b equal {}-{}*($a-1)\n'.format(
                    'variable', self.Tg_kwargs['Tinit'],
                    self.Tg_kwargs['Tinterval']))
                f.write(
                    '{:<15} fNPT all npt temp $b $b {} iso {} {} {}\n'.format(
                        'fix', self.Tg_kwargs['Tdamp'],
                        self.Tg_kwargs['pressure'], self.Tg_kwargs['pressure'],
                        self.Tg_kwargs['Pdamp']))
                f.write('{:<15} {}\n'.format('run', step))
                f.write('{:<15} fNPT\n'.format('unfix'))
                f.write('{:<15} a\n'.format('next'))
                f.write('{:<15} SELF loop\n'.format('jump'))
                f.write('{:<15} a delete\n'.format('variable'))
