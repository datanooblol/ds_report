import numpy as np
import pandas as pd

class ds_report(object):
    
    def __init__(self,dataframe):
        self._df = dataframe.copy()
        self._rows = []
        self._columns = []
    
    @property
    def df(self):
        return self._df
    
    @property
    def show_na(self):
        na_report = pd.DataFrame({
            'columns':list(self._df.isna().sum().index),
            'null':list(self._df.isna().sum()),
            'ratio':list(self._df.isna().sum()/len(self._df)*100)
        })
        return(na_report)
    
    @property
    def num_stats(self):
        desc_df = self._df.select_dtypes('number').describe().T
        desc_df['variance'] = self._df.select_dtypes('number').var()
        desc_df['skew'] = self._df.select_dtypes('number').skew()
        desc_df['kurtosis'] = self._df.select_dtypes('number').kurt()
        return(desc_df)
    
    @property
    def char_stats(self):
        desc_df = self._df.select_dtypes('object').describe().T
        return(desc_df)
    
    @property
    def data_types(self):
        dt_df = pd.DataFrame({
            'total':self._df.dtypes.apply(lambda x: str(x))
        }).total.value_counts().to_frame()
        return(dt_df)
    
    def to_char(self,cols):
        self._df[cols] = self._df[cols].astype('object')
    
    def to_cat(self,cols):
        self._df[cols] = self._df[cols].astype('category')

    def to_num(self,cols,func):
        func_dict = {'int8':np.int8, 'int16':np.int16, 'int32':np.int32, 'int64':np.int64,
                    'float16':np.float16,'float32':np.float32,'float64':np.float64}
        self._df[cols] = func_dict[func](self._df[cols])
    
    @property
    def report(self):
        self._rows.append(self._df.shape[0])
        self._columns.append(self._df.shape[1])
        shape_df = pd.DataFrame({
            'rows':self._rows,
            'columns':self._columns
        },index=['stage' + str(i) for i in range(len(self._rows))])
        return(shape_df)