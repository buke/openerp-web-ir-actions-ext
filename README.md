openerp-web-ir-actions-ext
==========================

关闭OpenERP 向导窗口后，回调JS 函数。

如::

        return {
            'type':'ir_actions_ext_afterclose',
            'obj':'inner_widget.room_list_widgets',
            'func':'refresh_room_info',
            'arg': [res_original.id],
        }
        
        

相当于关闭向导窗口后则执行 js 代码::

        self.inner_widget.room_list_widgets.refresh_room_info(res_original.id);



如果您觉得好用，请进入下面的网址，付费支持作者 ~

http://me.alipay.com/wangbuke

谢谢！


