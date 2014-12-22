# -*- coding: utf-8 -*-
##############################################################################
#
#    web ir actions extend
#    Copyright 2014 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'web ir.actions.ext',
    'version': '0.1',
    'category': 'Tools',
    'description': """

关闭OpenERP 向导窗口后，回调JS 函数。

如:

        return {
            'type':'ir_actions_ext_afterclose',
            'obj':'inner_widget.room_list_widgets',
            'func':'refresh_room_info',
            'arg': [res_original.id],
        }

相当于关闭向导窗口后则执行 js 代码:
        self.inner_widget.room_list_widgets.refresh_room_info(res_original.id);


如果您觉得好用，请进入下面的网址，付费支持作者 ~

http://me.alipay.com/wangbuke

谢谢！

""",
    'author': 'wangbuke@gmail.com',
    'website': 'http://buke.github.io',
    'depends': ['web'],
    'data': [
        'views/web_ir_actions_ext.xml',
    ],
    'installable': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
