<script>
  Ext.onReady(function(){
   var panel=new Ext.form.FormPanel({
    tbar:[{text:'提交',handler:function(){
         panel.getForm().submit({
          url:'FileUploadAction',
          success:function(){
            alert("上传成功!");
          }    
      });
         }
    }],
   
   fileUpload:true,
    items:[{xtype:'textfield',inputType:'file',fieldLabel:'图片上传',allowBlank:false}]
    });
   
 new Ext.Viewport( {
  layout : 'fit',
  items : [ panel ],
  renderTo : Ext.getBody()
 });
  });
 
        
</script>
