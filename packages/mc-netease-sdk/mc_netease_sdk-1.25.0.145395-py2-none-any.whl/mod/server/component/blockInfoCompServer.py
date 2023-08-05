# -*- coding: utf-8 -*-

from typing import Union
from typing import Tuple
from mod.common.component.baseComponent import BaseComponent
from typing import Any

class BlockInfoComponentServer(BaseComponent):
    def GetBlockLightLevel(self, pos, dimensionId=-1):
        # type: (Tuple[int,int,int], int) -> int
        """
        获取方块位置的光照等级
        """
        pass

    def SetBlockNew(self, pos, blockDict, oldBlockHandling=0, dimensionId=-1):
        # type: (Tuple[int,int,int], dict, int, int) -> bool
        """
        设置某一位置的方块
        """
        pass

    def PlayerDestoryBlock(self, pos, particle=1, sendInv=False):
        # type: (Tuple[int,int,int], int, bool) -> bool
        """
        使用手上工具破坏方块
        """
        pass

    def PlayerUseItemToPos(self, pos, posType, slotPos=0, facing=1):
        # type: (Tuple[int,int,int], int, int, int) -> bool
        """
        玩家对某个坐标使用物品
        """
        pass

    def PlayerUseItemToEntity(self, entityId):
        # type: (str) -> bool
        """
        玩家使用手上物品对某个生物使用
        """
        pass

    def GetBlockNew(self, pos, dimensionId=-1):
        # type: (Tuple[int,int,int], int) -> dict
        """
        获取某一位置的block
        """
        pass

    def GetTopBlockHeight(self, pos, dimension=0):
        # type: (Tuple[int,int], int) -> Union[int,None]
        """
        获取某一位置最高的非空气方块的高度
        """
        pass

    def CheckBlockToPos(self, fromPos, toPos, dimensionId=-1):
        # type: (Tuple[float,float,float], Tuple[float,float,float], int) -> int
        """
        判断位置之间是否有方块
        """
        pass

    def SetBlockTileEntityCustomData(self, pos, key, value):
        # type: (Tuple[int,int,int], str, Any) -> bool
        """
        设置指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。
        """
        pass

    def GetBlockTileEntityCustomData(self, pos, key):
        # type: (Tuple[int,int,int], str) -> Any
        """
        读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据
        """
        pass

    def GetBlockTileEntityWholeCustomData(self, pos):
        # type: (Tuple[int,int,int]) -> Union[dict,None]
        """
        读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据字典。
        """
        pass

    def CleanBlockTileEntityCustomData(self, pos):
        # type: (Tuple[int,int,int]) -> bool
        """
        清空指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。
        """
        pass

    def GetBlockEntityData(self, dimension, pos):
        # type: (int, Tuple[int,int,int]) -> Union[dict,None]
        """
        用于获取方块（包括自定义方块）的数据，数据只读不可写
        """
        pass

    def SpawnResourcesSilkTouched(self, identifier, pos, aux, dimensionId=-1):
        # type: (str, Tuple[int,int,int], int, int) -> bool
        """
        模拟方块精准采集掉落
        """
        pass

    def SpawnResources(self, identifier, pos, aux, probability=1.0, bonusLootLevel=0, dimensionId=-1, allowRandomness=True):
        # type: (str, Tuple[int,int,int], int, float, int, int, bool) -> bool
        """
        产生方块随机掉落（该方法不适用于实体方块）
        """
        pass

    def GetChestPairedPosition(self, pos):
        # type: (Tuple[int,int,int]) -> Union[Tuple[int,int,int],None]
        """
        获取与箱子A合并成一个大箱子的箱子B的坐标
        """
        pass

    def GetBedColor(self, pos):
        # type: (Tuple[int,int,int]) -> int
        """
        获取床（方块）的颜色
        """
        pass

    def SetBedColor(self, pos, color):
        # type: (Tuple[int,int,int], int) -> bool
        """
        设置床（方块）的颜色
        """
        pass

    def GetSignBlockText(self, pos):
        # type: (Tuple[int,int,int]) -> str
        """
        获取告示牌（方块）的文本内容
        """
        pass

    def SetSignBlockText(self, pos, text):
        # type: (Tuple[int,int,int], str) -> bool
        """
        设置告示牌（方块）的文本内容
        """
        pass

    def MayPlace(self, identifier, blockPos, facing, dimensionId=0):
        # type: (str, Tuple[int,int,int], int, int) -> bool
        """
        判断方块是否可以放置
        """
        pass

    def ListenOnBlockRemoveEvent(self, identifier, listen):
        # type: (str, bool) -> bool
        """
        是否监听方块BlockRemoveServerEvent事件，可以动态修改json组件netease:listen_block_remove的值
        """
        pass

    def GetDestroyTotalTime(self, blockName, itemName=None):
        # type: (str, str) -> float
        """
        获取使用物品破坏方块需要的时间
        """
        pass

    def RegisterOnStandOn(self, blockName, sendPythonEvent):
        # type: (str, bool) -> bool
        """
        可以动态注册与修改netease:on_stand_on组件
        """
        pass

    def UnRegisterOnStandOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_stand_on组件
        """
        pass

    def RegisterOnStepOn(self, blockName, sendPythonEvent):
        # type: (str, bool) -> bool
        """
        可以动态注册与修改netease:on_step_on组件
        """
        pass

    def UnRegisterOnStepOn(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_step_on组件
        """
        pass

    def RegisterOnStepOff(self, blockName, sendPythonEvent):
        # type: (str, bool) -> bool
        """
        可以动态注册与修改netease:on_step_off组件
        """
        pass

    def UnRegisterOnStepOff(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_step_off组件
        """
        pass

    def RegisterOnEntityInside(self, blockName, sendPythonEvent):
        # type: (str, bool) -> bool
        """
        可以动态注册与修改netease:on_entity_inside组件
        """
        pass

    def UnRegisterOnEntityInside(self, blockName):
        # type: (str) -> bool
        """
        可以动态删除netease:on_entity_inside组件
        """
        pass

