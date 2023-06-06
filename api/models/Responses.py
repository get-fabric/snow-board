from api.models.Models import *


class InboundResponse:
    invoices: int
    tote_types_number: int
    overall_lines: int
    items_to_decant: List[InfoPerToteType]

    def __init__(self, invoices: int, tote_types_number: int, overall_lines: int,
                 items_to_decant: [InfoPerToteType]):
        self.invoices = invoices
        self.overall_lines = overall_lines
        self.tote_types_number = tote_types_number
        self.items_to_decant = items_to_decant


class TotesStatusResponse:
    def __init__(self, totes_summery: List[ToteSummery]):
        super().__init__()
        self.totes_summery = totes_summery

    totes_summery: List[ToteSummery]


class SiteResourcesResponse:
    def __init__(self, tps: List[TPInfo]):
        self.tps = tps

    tps: List[TPInfo]


class OperationalTasksResponse:
    def __init__(self, qc: QC,
                 tote_extraction: ToteExtraction,
                 totes_can_be_optimized: ToteOptimization):
        super().__init__()
        self.qc = qc
        self.tote_extraction = tote_extraction
        self.totes_can_be_optimized = totes_can_be_optimized

    qc: QC
    tote_extraction: ToteExtraction
    totes_can_be_optimized: ToteOptimization


class OverviewResponse:
    def __init__(self, npr: int,
                 iph: int,
                 dph: int,
                 items_picked: int,
                 items_to_pick_total: int,
                 items_decanted: int,
                 items_to_decant_total: int,
                 items_qc: int,
                 items_to_qc_total: int):
        self.npr = npr
        self.iph = iph
        self.dph = dph
        self.items_picked = items_picked
        self.items_to_pick_total = items_to_pick_total
        self.items_decanted = items_decanted
        self.items_to_decant_total = items_to_decant_total
        self.items_qc = items_qc
        self.items_to_qc_total = items_to_qc_total

    # overview
    # maybe should be listed as avg per hour
    npr: int
    iph: int
    dph: int
    # drill down
    items_picked: int
    items_to_pick_total: int
    items_decanted: int
    items_to_decant_total: int
    items_qc: int
    items_to_qc_total: int
