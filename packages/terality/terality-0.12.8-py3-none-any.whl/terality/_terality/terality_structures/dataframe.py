from typing import Dict, Optional, List, Sequence, Hashable, Union

import pandas as pd

from common_client_scheduler import ExportRequest
from terality_serde import StructType

from . import ClassMethod, Struct
from ..data_transfers.common import S3


class ClassMethodDF(ClassMethod):
    _class_name: str = StructType.DATAFRAME
    _pandas_class = pd.DataFrame
    _additional_class_methods = ClassMethod._additional_class_methods | {
        "from_dict",
        "from_records",
    }


def _make_export_request(path: str, storage_options: Optional[Dict] = None) -> ExportRequest:
    if path.startswith("s3://"):
        bucket = path[5:].split("/", maxsplit=1)[0]
        aws_region = S3.client().get_bucket_location(Bucket=bucket)["LocationConstraint"]
    else:
        aws_region = None
    return ExportRequest(path=path, aws_region=aws_region, storage_options=storage_options)


class DataFrame(Struct, metaclass=ClassMethodDF):
    _class_name: str = StructType.DATAFRAME
    _pandas_class_instance = pd.DataFrame()
    _additional_methods = Struct._additional_methods | {
        "to_csv_folder",
        "to_parquet_folder",
    }
    _args_to_replace: dict = {
        # "to_csv" : (0, ExportRequest),
        "to_excel": (0, _make_export_request)
    }

    def _on_missing_attribute(self, item: str):
        return self._call_method(None, "df_col_by_attribute_access", item)

    def __iter__(self):
        # Iterating on a `DataFrame` is the same as iterating on its columns.
        return self.columns.__iter__()

    def to_csv(  # pylint: disable=too-many-arguments, too-many-locals
        self,
        path_or_buf: str,
        sep: str = ",",
        na_rep: str = "",
        float_format: Optional[str] = None,
        columns: Optional[Sequence[Optional[Hashable]]] = None,
        header: Union[bool, List[str]] = True,
        index: bool = True,
        index_label: Optional[Union[str, Sequence, bool]] = None,
        mode: str = "w",
        encoding: Optional[str] = None,
        compression: Union[str, dict] = "infer",
        quoting: Optional[int] = None,
        quotechar: str = '"',
        line_terminator: Optional[str] = None,
        chunksize: Optional[int] = None,
        date_format: Optional[str] = None,
        doublequote: bool = True,
        escapechar: Optional[str] = None,
        decimal: str = ".",
        errors: str = "strict",
        storage_options: Optional[Dict] = None,
    ) -> Optional[str]:
        export_request = _make_export_request(path_or_buf, storage_options)
        return self._call_method(
            None,
            "to_csv",
            export_request,
            sep=sep,
            na_rep=na_rep,
            float_format=float_format,
            columns=columns,
            header=header,
            index=index,
            index_label=index_label,
            mode=mode,
            encoding=encoding,
            compression=compression,
            quoting=quoting,
            quotechar=quotechar,
            line_terminator=line_terminator,
            chunksize=chunksize,
            date_format=date_format,
            doublequote=doublequote,
            escapechar=escapechar,
            decimal=decimal,
            errors=errors,
            storage_options=storage_options,
        )

    def to_csv_folder(self, path: str, num_files: int, storage_options: Optional[Dict] = None):
        export_request = _make_export_request(path, storage_options)
        return self._call_method(None, "to_csv_folder", export_request, num_files)

    def to_parquet(
        self,
        path: str,
        engine: str = "auto",
        compression: Optional[str] = "snappy",
        index: Optional[bool] = None,
        partition_cols: Optional[List[str]] = None,
        storage_options: Optional[Dict] = None,
    ):

        return self._call_method(
            None,
            "to_parquet",
            _make_export_request(path, storage_options),
            engine=engine,
            compression=compression,
            index=index,
            partition_cols=partition_cols,
            storage_options=storage_options,
        )

    def to_parquet_folder(self, path: str, num_files: int, storage_options: Optional[Dict] = None):
        export_request = _make_export_request(path, storage_options)
        return self._call_method(None, "to_parquet_folder", export_request, num_files)

    def to_dict(self):
        pd_df = self._call_method(None, "to_dict")
        return pd_df.to_dict()

    def info(
        self,
        verbose: Optional[bool] = None,
        max_cols: Optional[int] = None,
        memory_usage: Optional[Union[bool, str]] = None,
        null_counts: Optional[bool] = None,
    ):

        info = self._call_method(
            None,
            "info",
            verbose=verbose,
            max_cols=max_cols,
            memory_usage=memory_usage,
            null_counts=null_counts,
        )
        print(info)
