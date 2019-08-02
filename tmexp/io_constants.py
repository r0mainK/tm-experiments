from typing import Counter as CounterType, Dict, List, NamedTuple, Set

DATASET_DIR = "/data/datasets"


class FileInfo(NamedTuple):
    blob_hash: str
    language: str


RefInfo = Dict[str, FileInfo]


class FilesInfo(Dict[str, RefInfo]):
    def __init__(self, refs: List[str]):
        super().__init__()
        for ref in refs:
            self[ref] = {}

    def remove(self, file_path: str, blob_hash: str) -> None:
        for ref_dict in self.values():
            if file_path in ref_dict and blob_hash == ref_dict[file_path].blob_hash:
                ref_dict.pop(file_path)


WordCount = CounterType[str]
FeatureContent = Dict[str, WordCount]
BlobContent = Dict[str, FeatureContent]


class FilesContent(Dict[str, BlobContent]):
    def __init__(self, files_info: FilesInfo):
        super().__init__()
        for ref_dict in files_info.values():
            for file_path in ref_dict:
                self[file_path] = {}

    def purge(self, blacklist: Set[str]) -> None:
        for file_path in blacklist:
            self.pop(file_path)


class Dataset(NamedTuple):
    files_info: Dict[str, FilesInfo] = {}
    files_content: Dict[str, FilesContent] = {}
    refs: Dict[str, List[str]] = {}


BOW_DIR = "/data/bows"
DOC_FILENAME = "doc.bow_tm.txt"
DOCWORD_FILENAME = "docword.bow_tm.txt"
REF_FILENAME = "refs.bow_tm.txt"
VOCAB_FILENAME = "vocab.bow_tm.txt"

TOPICS_DIR = "/data/topics"
DOCTOPIC_FILENAME = "doctopic.npy"
WORDTOPIC_FILENAME = "wordtopic.npy"
MEMBERSHIP_FILENAME = "membership.pkl"
WORDCOUNT_FILENAME = "wordcount.pkl"
METRICS_FILENAME = "metrics.pkl"
LABELS_FILENAME = "labels.txt"

VIZ_DIR = "/data/visualisations"
HEATMAP_FILENAME = "heatmap_%s.png"
EVOLUTION_FILENAME = "topic_%d.png"
