from ..base import Base


class Aggregate(Base):
    """Aggregate service"""

    def aggregate(
        self,
        dataset_id: str,
        metrics: list = [],
        groupby: list = [],
        filters: list = [],
        page_size: int = 20,
        page: int = 1,
        asc: bool = False,
        flatten: bool = True,
        alias: str = "default",
    ):
        return self.make_http_request(
            "services/aggregate/aggregate",
            method="POST",
            parameters={
                "dataset_id": dataset_id,
                "aggregation_query": {"groupby": groupby, "metrics": metrics},
                "filters": filters,
                "page_size": page_size,
                "page": page,
                "asc": asc,
                "flatten": flatten,
                "alias": alias,
            },
        )
