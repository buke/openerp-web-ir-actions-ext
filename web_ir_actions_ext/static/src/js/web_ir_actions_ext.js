/*---------------------------------------------------------
 * web ir actions extend
 * Copyright 2014 wangbuke <wangbuke@gmail.com>
 *---------------------------------------------------------*/
openerp.web_ir_actions_ext = function(instance) {
    instance.web.ActionManager = instance.web.ActionManager.extend({
        // call js
        ir_actions_ext_afterclose: function (action, options) {
            var self = this;
            if (!this.dialog) {
                options.on_close();
            }
            this.dialog_stop();

            var obj_list = action.obj.split('.');
            var obj = self;
            for (var i=0;i<obj_list.length;i++){
                obj = obj[obj_list[i]];
            }
            
            var func = obj[action.func];
            var arg = action.arg || [];

            return func.apply(obj, arg);
        },

    });

};

// vim:et fdc=0 fdl=0 foldnestmax=3 fdm=syntax:
