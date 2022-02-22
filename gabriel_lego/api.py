import enum
from typing import List, Sequence

import nptyping as npt

from .cv import image_util as img_util
from .cv.lego_cv import LEGOCVError, LowConfidenceError, \
    NoBoardDetectedError, \
    NoLEGODetectedError
from .lego_engine.board import BoardState, EmptyBoardState
from .lego_engine.task_manager import InitialTaskState, \
    NoStateChangeError

__all__ = [
    'FrameResult', 'TaskIsFinished', 'LEGOTask'
]


class FrameResult(enum.Enum):
    SUCCESS = enum.auto()
    TASK_ERROR = enum.auto()
    CV_ERROR = enum.auto()
    LOW_CONFIDENCE = enum.auto()
    JUNK_FRAME = enum.auto()
    NO_CHANGE = enum.auto()


class TaskIsFinished(Exception):
    def __init__(self):
        super(TaskIsFinished, self).__init__()


class LEGOTask:
    def __init__(self, step_bitmaps: Sequence[npt.NDArray]):
        super(LEGOTask, self).__init__()

        board_states: List[BoardState] = [EmptyBoardState()]
        board_states += [BoardState(b) for b in step_bitmaps]
        self._state = InitialTaskState(board_states)
        self._task_len = len(board_states)

    @property
    def task_length(self) -> int:
        return self._task_len

    def get_current_guide_illustration(self) -> npt.NDArray:
        return self._state.current_image.copy()

    def get_current_instruction(self) -> str:
        return self._state.current_instruction

    @property
    def finished(self) -> bool:
        return self._state.is_final

    def submit_frame(self, img_frame: npt.NDArray) -> FrameResult:
        if self._state.is_final:
            raise TaskIsFinished()

        try:
            try:
                board_state = BoardState(img_util.preprocess_img(img_frame))
            except NoLEGODetectedError:
                # board is in frame, but it's empty
                board_state = EmptyBoardState()

            # *actually* compute next state
            self._state = self._state.compute_next_task_state(board_state)
            return FrameResult.SUCCESS \
                if self._state.is_correct else \
                FrameResult.TASK_ERROR
        except LowConfidenceError:
            return FrameResult.LOW_CONFIDENCE
        except NoBoardDetectedError:
            # junk frame, no board in frame
            return FrameResult.JUNK_FRAME
        except LEGOCVError:
            # other CV error
            return FrameResult.CV_ERROR
        except NoStateChangeError:
            return FrameResult.NO_CHANGE
