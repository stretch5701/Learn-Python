'''
    Container for ZipBu class.  A class for backing up folders as zip files
    using shutil.make_archive
'''


from datetime import datetime as dt
from pathlib import Path as p
import os, shutil



class RkWrapper:
    '''
        Wrapper for shutil.make_archive.  Adds option of a destination
        path.
        
        if set, working directory is set to dest. If None then users home
        directory is used.  Note: Shutil.make_archive write archive file to
        working directory.
    
    '''
    
    def __init__(self, root = None, source = None, dest = None):
        self.root = root
        self.source = source
        if dest == None:
            self.dest = p.home()
        else:
            self.dest = dest
            
        assert (self.root != None), 'root cannot be None'

        os.chdir(self.dest)  #destination folder for zip file.
        

    def build_fname(self):
        '''
            Uses datetime to create "YYYYMMDD" to append to filename of
            zipped backup file. If source is set final filename is of
            the form: "sourceBU_YYYYMMDD.zip".  If not then the basename
            for root is used: "rootBU_yyyymmdd"
        '''
        
        _now = ''.join(str(dt.date(dt.now())).split('-')) #YYYYMMDD

        if self.source == None:
            bu_name = os.path.basename(self.root) + 'BU_' + _now
        else:
            bu_name = os.path.basename(self.source) + 'BU_' + _now
        return bu_name

    def createBU(self):
        '''
            Creates backup archive as a zip file.  Root_dir is root to
            directory that is to be archived.  base_dir is directory that
            is to be archived and set to source, such that full path would be:
            "root//source"  Zip file is saved in users working directory
            (set to home as default).
        '''
        
        bu_name = self.build_fname() 
        shutil.make_archive(bu_name,
                            'zip',
                            root_dir = self.root,
                            base_dir = self.source)



if __name__ == '__main__':

    
    save_cwd = p.cwd()
    
    rpr = RkWrapper(root = r'E:\MyPython')
#     rpr = RkWrapper(root = None)
    rpr.createBU()
    
    os.chdir(save_cwd)
