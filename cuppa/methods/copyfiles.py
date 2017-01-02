
#          Copyright Jamie Allsop 2016
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

#-------------------------------------------------------------------------------
#   CopyFilesMethod
#-------------------------------------------------------------------------------

import os.path
import cuppa.progress


class CopyFilesMethod:

    def __call__( self, env, target, source ):
        destination = target
        if destination[0] != '#' and not os.path.isabs( destination ):
            destination = os.path.join( env['abs_final_dir'], destination )
        installed_files = env.Install( destination, source )
        cuppa.progress.NotifyProgress.add( env, installed_files )
        return installed_files

    @classmethod
    def add_to_env( cls, cuppa_env ):
        cuppa_env.add_method( "CopyFiles", cls() )

