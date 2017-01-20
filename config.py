root = {
# 2个字节长度, type = LEN 表示后面的总字节长度
    -6: { 'name': '报文长度', 'class': 'V', 'type': 'LEN', 'len': 2, 'code': 'BYTES'},
    -5: { 'name': 'TPDU',    'class': 'V',  'type': 'N', 'len': 5, 'code': 'ASCII'},
    -4: { 'name': '网络标志', 'class': 'V', 'type': 'N', 'len': 2, 'code': 'ASCII'},
    -3: { 'name': '交易流水', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    -2: { 'name': '错误代码', 'class': 'V', 'type': 'N', 'len': 4, 'code': 'ASCII'},
    -1: { 'name': '消息类型', 'class': 'V', 'type': 'N', 'len': 4, 'code': 'ASCII'},
# 位图自动计算
    0: { 'name': '位图', 'class': 'V', 'type': 'N', 'len': 16, 'code': 'BYTES'},
    2: { 'name': '主账号', 'class': 'LLV', 'type': 'N', 'len': 19, 'code': 'ASCII'},
    3: { 'name': '交易处理码', 'class': 'V', 'type': 'N', 'len': 6, 'code': 'ASCII'},
    4: { 'name': '交易金额', 'class': 'V', 'type': 'N', 'len': 12, 'code': 'ASCII'},
    7: { 'name': '渠道标识码', 'class': 'V', 'type': 'AN', 'len': 2, 'code': 'ASCII'},
    11: { 'name': '流水号', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    12: { 'name': '本地时间', 'class': 'V', 'type': 'N', 'len': 6, 'code': 'ASCII'},
    13: { 'name': '本地日期', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    14: { 'name': '卡有效期', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    15: { 'name': '清算日期', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    16: { 'name': '存期', 'class': 'V', 'type': 'N', 'len': 2, 'code': 'ASCII'},
    18: { 'name': '商户类型', 'class': 'V', 'type': 'N', 'len': 6, 'code': 'ASCII'},
    20: { 'name': '交易标志', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},

    21: { 'name': '加钞内容', 'class': 'V', 'type': 'AN', 'len': 36, 'code': 'ASCII'},
    22: { 'name': '服务点进入方式', 'class': 'V', 'type': 'N', 'len': 3, 'code': 'ASCII'},
    23: { 'name': '卡序列号', 'class': 'V', 'type': 'N', 'len': 3, 'code': 'ASCII'},
    24: { 'name': '终端状态信息', 'class': 'V', 'type': 'AN', 'len': 80, 'code': 'ASCII'},
    25: { 'name': '服务点条件代码', 'class': 'V', 'type': 'N', 'len': 2, 'code': 'ASCII'},
    28: { 'name': '手续费1', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    29: { 'name': '手续费2', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},
    30: { 'name': '手续费3', 'class': 'V', 'type': 'N', 'len': 8, 'code': 'ASCII'},

    35: { 'name': '第二磁道数据', 'class': 'LLV', 'type': 'Z', 'len': 37, 'code': 'ASCII'},
    36: { 'name': '第三磁道数据', 'class': 'LLLV', 'type': 'Z', 'len': 104, 'code': 'ASCII'},
    37: { 'name': '检索参考号', 'class': 'V', 'type': 'N', 'len': 12, 'code': 'ASCII'},
    38: { 'name': '授权标识响应码', 'class': 'V', 'type': 'N', 'len': 16, 'code': 'ASCII'},
    39: { 'name': '响应码', 'class': 'V', 'type': 'N', 'len': 2, 'code': 'ASCII'},
    40: { 'name': '开户行信息', 'class': 'LLV', 'type': 'ANS', 'len': 51, 'code': 'ASCII'},

    41: { 'name': '终端标识号', 'class': 'V', 'type': 'ANS', 'len': 8, 'code': 'ASCII'},
    42: { 'name': '受卡方标识号', 'class': 'V', 'type': 'ANS', 'len': 15, 'code': 'ASCII'},
    45: { 'name': '附加数据', 'class': 'LLLV', 'type': 'ANS', 'len': 512, 'code': 'ASCII'},
    46: { 'name': '存折印刷号', 'class': 'V', 'type': 'ANS', 'len': 10, 'code': 'ASCII'},
    49: { 'name': '交易货币代码', 'class': 'V', 'type': 'AN', 'len': 3, 'code': 'ASCII'},

    51: { 'name': '柜员号', 'class': 'V', 'type': 'N', 'len': 7, 'code': 'ASCII'},
    52: { 'name': '个人识别号密文', 'class': 'V', 'type': 'B', 'len': 8, 'code': 'BYTES'},
    53: { 'name': '安全控制信息', 'class': 'V', 'type': 'N', 'len': 16, 'code': 'ASCII'},
    54: { 'name': '附加余额', 'class': 'V', 'type': 'AN', 'len': 39, 'code': 'ASCII'},
    55: { 'name': 'IC卡数据域', 'class': 'LLLV', 'type': 'ANS', 'len': 255, 'code': 'BYTES'},
    59: { 'name': '扩展消息原因码', 'class': 'LLLV', 'type': 'ANS', 'len': 100, 'code': 'ASCII'},

    60: { 'name': '消息原因码', 'class': 'V', 'type': 'N', 'len': 4, 'code': 'ASCII'},
    61: { 'name': '客户消息', 'class': 'LLV', 'type': 'ANS', 'len': 54, 'code': 'ASCII'},
    62: { 'name': '附加个人标识号数据', 'class': 'V', 'type': 'B', 'len': 8, 'code': 'BYTES'},
    63: { 'name': '证件信息', 'class': 'LLV', 'type': 'ANS', 'len': 22, 'code': 'ASCII'},
    68: { 'name': '票据号码', 'class': 'LLV', 'type': 'AN', 'len': 20, 'code': 'ASCII'},

    72: { 'name': '批次号', 'class': 'V', 'type': 'N', 'len': 4, 'code': 'ASCII'},
    90: { 'name': '原始交易信息', 'class': 'V', 'type': 'AN', 'len': 40, 'code': 'ASCII'},
    93: { 'name': '响应标识符', 'class': 'V', 'type': 'AN', 'len': 3, 'code': 'ASCII'},
    96: { 'name': '报文安全码', 'class': 'LLV', 'type': 'B', 'len': 24, 'code': 'BYTES'},

    102: { 'name': '附加账号', 'class': 'LLV', 'type': 'ANS', 'len': 100, 'code': 'ASCII'},
    103: { 'name': '转入账号', 'class': 'LLV', 'type': 'ANS', 'len': 100, 'code': 'ASCII'},
    106: { 'name': ' 汇票附加标志', 'class': 'V', 'type': 'AN', 'len': 16, 'code': 'ASCII'},
    113: { 'name': '密钥信息', 'class': 'LLLV', 'type': 'ANS', 'len': 999, 'code': 'ASCII'},

    120: { 'name': '附加信息', 'class': 'LLLV', 'type': 'ANS', 'len': 999, 'code': 'ASCII'},
    121: { 'name': '对账信息', 'class': 'LLLV', 'type': 'ANS', 'len': 999, 'code': 'ASCII'},
    122: { 'name': '发起自定义数据', 'class': 'LLLV', 'type': 'ANS', 'len': 999, 'code': 'ASCII'},
    123: { 'name': '应答自定义数据', 'class': 'LLLV', 'type': 'ANS', 'len': 999, 'code': 'ASCII'},
    124: { 'name': '证书信息', 'class': 'LLLLV', 'type': 'ANS', 'len': 4095, 'code': 'ASCII'},
    127: { 'name': '终端状态定义内容', 'class': 'LLLV', 'type': 'ANS', 'len': 126, 'code': 'ASCII'},
    128: { 'name': '密钥信息', 'class': 'V', 'type': 'B', 'len': 16, 'code': 'BYTES'},

}

fields = {
    24: {
        1: { 'name': '出钞模块状态', 'len': 1},
        2: { 'name': '存款模块状态', 'len': 1},
        3: { 'name': 'IC 卡读卡器状态', 'len': 1},
        4: { 'name': '磁条卡读卡器状态', 'len': 1},
        5: { 'name': '保险门', 'len': 1},
        6: { 'name': '用户键盘', 'len': 1},
        7: { 'name': '显示器', 'len': 1},
        8: { 'name': '加密模块', 'len': 1},
        9: { 'name': '主控板', 'len': 1},
        10: { 'name': '票据打印机', 'len': 1},
        11: { 'name': '语音模块', 'len': 1},
        12: { 'name': '存折打印机状态', 'len': 1},
        13: { 'name': '信封打印机状态', 'len': 1},
        14: { 'name': '录像机状态', 'len': 1},
        15: { 'name': '第 1 摄像头状态', 'len': 1},
        16: { 'name': '第 2 摄像头状态', 'len': 1},
        17: { 'name': '第 3 摄像头状态', 'len': 1},
        18: { 'name': '流水打印机状态', 'len': 1},
        19: { 'name': '凭条打印机 1 状态', 'len': 1},
        20: { 'name': '录像硬盘状态', 'len': 1},
        21: { 'name': '钞箱 1 状态', 'len': 1},
        22: { 'name': '钞箱 2 状态', 'len': 1},
        23: { 'name': '钞箱 3 状态', 'len': 1},
        24: { 'name': '钞箱 4 状态', 'len': 1},
        25: { 'name': '钞箱 5 状态', 'len': 1},
        26: { 'name': '钞箱 6 状态', 'len': 1},
        27: { 'name': '存款钞箱状态', 'len': 1},
        28: { 'name': '废钞箱状态', 'len': 1},
        29: { 'name': '钞箱 1 张数', 'len': 4},
        30: { 'name': '钞箱 2 张数', 'len': 4},
        31: { 'name': '钞箱 3 张数', 'len': 4},
        32: { 'name': '钞箱 4 张数', 'len': 4},
        33: { 'name': '钞箱 5 张数', 'len': 4},
        34: { 'name': '钞箱 6 张数', 'len': 4},
        35: { 'name': '废钞箱张数', 'len': 4},
        36: { 'name': '钞箱 1 面值/币种', 'len': 2},
        37: { 'name': '钞箱 2 面值/币种', 'len': 2},
        38: { 'name': '钞箱 3 面值/币种', 'len': 2},
        39: { 'name': '钞箱 4 面值/币种', 'len': 2},
        40: { 'name': '钞箱 5 面值/币种', 'len': 2},
        41: { 'name': '钞箱 6 面值/币种', 'len': 2},
        42: { 'name': '机器状态', 'len': 1},
        43: { 'name': '吞卡数', 'len': 2},
        44: { 'name': '自劣设备软件版本号', 'len': 4},
        45: { 'name': '预留', 'len': 5},
    },

    54: {
        1: { 'name': '账户余额', 'len': 13},
        2: { 'name': '存折余额', 'len': 13},
        3: { 'name': '可用余额', 'len': 13},
    },

    127: {
        1: { 'name': '产品代码', 'len': 6},
        2: { 'name': '存/取钞模块状态', 'len': 1},
        3: { 'name': '非接触读卡器状态', 'len': 1},
        4: { 'name': '接触式读卡器状态', 'len': 1},
        5: { 'name': '读卡器异形口状态', 'len': 1},
        6: { 'name': '保险门', 'len': 1},
        7: { 'name': '用户键盘', 'len': 1},
        8: { 'name': '显示器', 'len': 1},
        9: { 'name': '加密模块', 'len': 1},
        10: { 'name': '主控板', 'len': 1},
        11: { 'name': '票据打印机', 'len': 1},
        12: { 'name': '语音模块', 'len': 1},
        13: { 'name': '存折打印机状态', 'len': 1},
        14: { 'name': '信封打印机状态', 'len': 1},
        15: { 'name': '录像机状态', 'len': 1},
        16: { 'name': '第 1 摄像头状态', 'len': 1},
        17: { 'name': '第 2 摄像头状态', 'len': 1},
        18: { 'name': '第 3 摄像头状态', 'len': 1},
        19: { 'name': '第 4 摄像头状态', 'len': 1},
        20: { 'name': '第 5 摄像头状态', 'len': 1},
        21: { 'name': '第 6 摄像头状态', 'len': 1},
        22: { 'name': '流水打印机状态', 'len': 1},
        23: { 'name': '凭条打印机 1 状态', 'len': 1},
        24: { 'name': '录像硬盘状态', 'len': 1},
        25: { 'name': '钞箱 1 状态', 'len': 1},
        26: { 'name': '钞箱 2 状态', 'len': 1},
        27: { 'name': '钞箱 3 状态', 'len': 1},
        28: { 'name': '钞箱 4 状态', 'len': 1},
        29: { 'name': '钞箱 5 状态', 'len': 1},
        30: { 'name': '钞箱 6 状态', 'len': 1},
        31: { 'name': '废钞箱状态（含回收箱）', 'len': 1},
        32: { 'name': '整机存款状态', 'len': 1},
        33: { 'name': '整机取款状态', 'len': 1},
        34: { 'name': '废钞箱业务状态（含回收箱）', 'len': 1},
        35: { 'name': '钞箱 1 张数', 'len': 4},
        36: { 'name': '钞箱 2 张数', 'len': 4},
        37: { 'name': '钞箱 3 张数', 'len': 4},
        38: { 'name': '钞箱 4 张数', 'len': 4},
        39: { 'name': '钞箱 5 张数', 'len': 4},
        40: { 'name': '钞箱 6 张数', 'len': 4},
        41: { 'name': '废钞箱张数', 'len': 4},
        42: { 'name': '钞箱 1 面值/币种', 'len': 2},
        43: { 'name': '钞箱 2 面值/币种', 'len': 2},
        44: { 'name': '钞箱 3 面值/币种', 'len': 2},
        45: { 'name': '钞箱 4 面值/币种', 'len': 2},
        46: { 'name': '钞箱 5 面值/币种', 'len': 2},
        47: { 'name': '钞箱 6 面值/币种', 'len': 2},
        48: { 'name': '机器状态', 'len': 1},
        49: { 'name': '吞卡数', 'len': 2},
        50: { 'name': '自助设备软件版本号', 'len': 4},
        51: { 'name': '总行广告版本号', 'len': 6},
        52: { 'name': '分行广告版本号', 'len': 6},
        53: { 'name': '资费标准公告版本号', 'len': 6},
        54: { 'name': '预留', 'len': 5},

    }


}

tran_code =  [['查询余额', '0200', '0210', '100100'],
 ['查询交易明细', '0200', '0210', '100200'],
 ['查询未登折明细', '0200', '0210', '100300'],
 ['绿卡通其它储种子帐户查询', '0200', '0210', '100400'],
 ['IC卡绑定借记账户查询', '0200', '0210', '100600'],
 ['电子银行客户信息查询', '0200', '0210', '100700'],
 ['密码验证查询', '0200', '0210', '100800'],
 ['本行户名查询', '0200', '0210', '100900'],
 ['跨行户名查询', '0200', '0210', '101000'],
 ['取款', '0200', '0210', '110100'],
 ['取款冲正', '0420', '0430', '110230'],
 ['存款', '0200', '0210', '110300'],
 ['存款重发', '0220', '0230', '110440'],
 ['转账', '0200', '0210', '110500'],
 ['不同储种转账', '0200', '0210', '110600'],
 ['Ic卡现金充值', '0200', '0210', '111000'],
 ['IC卡现金充值冲正', '0420', '0430', '111200'],
 ['Ic卡指定账户圈存', '0200', '0210', '111100'],
 ['Ic卡指定账户圈存冲正', '0420', '0430', '111300'],
 ['消费', '0200', '0210', '120100'],
 ['消费冲正', '0420', '0430', '120230'],
 ['消费撤销', '0200', '0210', '120320'],
 ['消费撤销冲正', '0420', '0430', '120430'],
 ['退货', '0220', '0230', '120500'],
 ['退货重发', '0220', '0230', '120640'],
 ['预授权', '0100', '0110', '130100'],
 ['预授权冲正', '0420', '0430', '130230'],
 ['追加预授权', '0100', '0110', '130300'],
 ['追加预授权冲正', '0420', '0430', '130430'],
 ['预授权撤销', '0100', '0110', '130520'],
 ['预授权撤销冲正', '0420', '0430', '130630'],
 ['预授权完成', '0200', '0210', '130700'],
 ['预授权完成冲正', '0420', '0430', '130830'],
 ['预授权完成撤销', '0200', '0210', '130920'],
 ['预授权完成撤销冲正', '0420', '0430', '131030'],
 ['离线预授权完成', '0220', '0230', '131100'],
 ['应缴费用查询', '0200', '0210', '140100'],
 ['代理缴费', '0200', '0210', '140200'],
 ['已缴费用查询', '0200', '0210', '140300'],
 ['预存缴费', '0200', '0210', '140400'],
 ['预存余额查询', '0200', '0210', '140500'],
 ['加办', '0200', '0210', '140600'],
 ['加办信息查询', '0200', '0210', '140700'],
 ['撤办', '0200', '0210', '140800'],
 ['代售交易', '0200', '0210', '140900'],
 ['代售查询', '0200', '0210', '141000'],
 ['发票打印', '0200', '0210', '141100'],
 ['异常通知', '0420', '0430', '141200'],
 ['自定义交易', '0200', '0210', '141300'],
 ['ATM自助开通任意电子渠道', '0200', '0210', '141400'],
 ['修改密码', '0200', '0210', '150100'],
 ['补登折', '0200', '0210', '150200'],
 ['新补登折', '0200', '0210', '150201'],
 ['对账簿打印', '0200', '0210', '150600'],
 ['卡折挂失', '0200', '0210', '150300'],
 ['IC卡修改小额支付余额上限', '0600', '0610', '150400'],
 ['获取短信验证码', '0200', '0210', '150500'],
 ['签到', '0820', '0830', '160100'],
 ['签退', '0820', '0830', '160200'],
 ['初始传输密钥', '0820', '0830', '160300'],
 ['终端更新密钥', '0820', '0830', '160400'],
 ['设备例外通知', '0820', '0830', '160500'],
 ['状态通知', '0820', '0830', '160600'],
 ['账户例外通知', '0820', '0830', '160700'],
 ['配钞', '0820', '0830', '160800'],
 ['平台更新密钥', '0820', '0830', '160900'],
 ['平台更新密钥确认', '0820', '0830', '161000'],
 ['脚本处理结果通知', '0820', '0830', '161100'],
 ['上送吞没卡记录', '0820', '0830', '161200'],
 ['轧账方式参数维护', '0820', '0830', '161300'],
 ['轧账', '0800', '0810', '170100'],
 ['上送对帐明细', '0800', '0810', '170200'],
 ['发票轧账', '0800', '0810', '170300'],
 ['POS结算', '0800', '0810', '170400'],
 ['POS对帐明细上送', '0800', '0810', '170500'],
 ['预轧帐', '0800', '0810', '170600'],
 ['预约汇款信息查询', '9100', '9110', '180100'],
 ['汇款', '9100', '9110', '180200'],
 ['汇款记录查询', '9100', '9110', '180300'],
 ['退汇申请', '9120', '9130', '180400'],
 ['汇票信息查询', '9100', '9110', '180500'],
 ['兑付入帐', '9100', '9110', '180600'],
 ['汇兑异常通知', '9120', '9130', '180700'],
 ['控制参数下载', '0800', '0810', '190100'],
 ['卡表下载', '0800', '0810', '190200'],
 ['代理交易画面导航参数下载', '0800', '0810', '190300'],
 ['IC卡卡表下载', '0800', '0810', '190400'],
 ['PBOC应用参数下载', '0800', '0810', '190500'],
 ['AID应用参数下载', '0800', '0810', '190600'],
 ['电子协议画面导航参数下载', '0800', '0810', '190700'],
 ['电子协议内容下载', '0800', '0810', '190800'],
 ['理财品种下载', '0800', '0810', '190901'],
 ['理财净值下载', '0800', '0810', '190901'],
 ['基金代销品种下载', '0800', '0810', '190901'],
 ['基金净值下载', '0800', '0810', '190901'],
 ['月月升同步文件下载', '0800', '0810', '190901'],
 ['SFTP基金理财文件下载', '0800', '0810', '190910'],
 ['逻辑开机', '0820', '0830', '200100'],
 ['逻辑关机', '0820', '0830', '200200'],
 ['热启动', '0820', '0830', '200300'],
 ['运行状态检测', '0820', '0830', '200400'],
 ['强制检查', '0820', '0830', '200500'],
 ['广告画面下发通知', '0820', '0830', '200600'],
 ['广告画面下发', '0820', '0830', '200700'],
 ['提取远程流水通知', '0820', '0830', '200800'],
 ['提取远程流水', '0820', '0830', '200900'],
 ['软件更新通知', '0820', '0830', '201000'],
 ['软件更新', '0820', '0830', '201100'],
 ['个人客户资料修改', '0000', '0010', '701090'],
 ['理财类业务在线签约', '0000', '0010', '701350'],
 ['理财产品认购', '0000', '0010', '702020'],
 ['理财产品撤单', '0000', '0010', '702000'],
 ['理财产品提前赎回', '0000', '0010', '702040'],
 ['理财产品终止投资', '0000', '0010', '702050'],
 ['修改密码', '0000', '0010', '701220'],
 ['理财产品交易明细查询', '0000', '0010', '702120'],
 ['理财产品帐户余额查询', '0000', '0010', '702110'],
 ['基金TA账户开户', '0000', '0010', '701250'],
 ['基金份额查询', '0000', '0010', '701100'],
 ['基金购买', '0000', '0010', '701030'],
 ['基金交易明细查询', '0000', '0010', '701110'],
 ['基金交易撤单', '0000', '0010', '701000'],
 ['基金赎回', '0000', '0010', '701050'],
 ['基金可赎回明细查询', '0000', '0010', '701390'],
 ['基金定期定额明细信息', '0000', '0010', '701190'],
 ['基金定期定期定额明细信息', '0000', '0010', '701200'],
 ['基金定期定额申购', '0000', '0010', '701160'],
 ['基金定期定额变更', '0000', '0010', '701170'],
 ['基金定期定额撤单', '0000', '0010', '701180'],
 ['根据证件查询中间帐户基本信息', '0000', '0010', '701310'],
 ['基金TA账号查询', '0000', '0010', '701130'],
 ['客户开通情况查询', '0200', '0210', '121100'],
 ['电子银行账户效验查询', '0200', '0210', '121200'],
 ['电子银行信用卡验密查询', '0200', '0210', '121300'],
 ['已签约账户校验查询', '0200', '0210', '121400'],
 ['申请授权', '0200', '0210', '121500'],
 ['根据证件信息查询理财卡号', '0200', '0210', '121600'],
 ['新客户账户开通渠道', '0200', '0210', '121700'],
 ['授权结果查询', '0200', '0210', '121800'],
 ['日常扫描', '0200', '0210', '121900'],
 ['追加扫描', '0200', '0210', '122000'],
 ['建立连接', '0200', '0210', '122100'],
 ['授权提交', '0200', '0210', '122200'],
 ['获取短信验证码', '0200', '0210', '122300'],
 ['校验手机验证码', '0200', '0210', '122400'],
 ['查询客户开卡数量', '0200', '0210', '101100'],
 ['客户信息查询', '0200', '0210', '101200'],
 ['客户信息创建', '0200', '0210', '141500'],
 ['客户信息修改', '0200', '0210', '141600'],
 ['卡申请', '0200', '0210', '141700'],
 ['轧凭证', '0800', '0810', '170101'],
 ['配凭证', '0820', '0830', '160801'],
 ['预扎凭证', '0800', '0810', '170601'],
 ['电子银行凭证类型查询', '0000', '0010', '615280'],
 ['电子银行凭证补发', '0000', '0010', '615640'],
 ['电子银行认证工具查询', '0000', '0010', '615270'],
 ['电子银行认证工具变更', '0000', '0010', '615650'],
 ['换卡', '0000', '0010', '615500'],
 ['自助渠道转账开通', '0000', '0010', '615370'],
 ['密码挂失', '0000', '0010', '615030'],
 ['密码重置', '0000', '0010', '615510'],
 ['再挂失', '0000', '0010', '615520'],
 ['账户对账单查询打印', '0000', '0010', '610390'],
 ['客户子账户查询', '0000', '0010', '610310'],
 ['自助交易限额设置', '0000', '0010', '615660'],
 ['开通短信通知交易', '0000', '0010', '610101'],
 ['结汇', '0000', '0010', '710101'],
 ['售汇', '0000', '0010', '710103'],
 ['外币兑换', '0000', '0010', '710130'],]
