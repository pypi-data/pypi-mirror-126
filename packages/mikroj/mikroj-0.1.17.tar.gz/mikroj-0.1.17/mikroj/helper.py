from mikro.schema import Representation
from mikroj.registries.helper import BaseImageJHelper, set_running_helper
import dask
import xarray as xr

class ImageJHelper(BaseImageJHelper):

    def __init__(self, headless=False, bind=True, version="sc.fiji:fiji:2.1.0", plugins = []) -> None:
        if bind: set_running_helper(self)
        super().__init__(headless=headless, version=version, plugins= plugins)


    def show_xarray(self, xarray: xr.DataArray):
        if dask.is_dask_collection(xarray.data):
            jimage = self.py.to_java(xarray.compute())
        else:
            jimage = self.py.to_java(xarray)
        
        self.ui.show(xarray.name, jimage)



    def displayRep(self, rep: Representation):
        image = rep.data.squeeze()

        if dask.is_dask_collection(image.data):
            jimage = self.py.to_java(image.compute())
        else:
            jimage = self.py.to_java(image)

        # Convert the Image to Image
        self.ui.show(rep.name, jimage)