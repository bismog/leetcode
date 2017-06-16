// http://www.programgo.com/article/67823642035/
 protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  response.setContentType("text/html");
  DiskFileItemFactory diskFile=new DiskFileItemFactory(); //磁盘工厂管理类
  diskFile.setSizeThreshold(1024*4);                      //设置磁盘内存临界区域
  diskFile.setRepository(new File("D:/"));               //设置图片缓存存放的位置
  
  ServletFileUpload fileUpload= new ServletFileUpload(diskFile);   //创建一个servlet 上传图片
  fileUpload.setSizeMax(1024*1024*2);                      //设置文件大小
  List fileList=null;                                    
  FileItem  item=null;                                 
  try{
   fileList=fileUpload.parseRequest(request);            //将request转换为FileItem的List集合
   Iterator<FileItem> it=fileList.iterator();            //迭代集合中的文件项
   while (it.hasNext()) {
     item = it.next();
     if(item.isFormField()){                             //判断是不是文件上传
      continue;
     }
     if(item.getName().equals("")||item.getSize()==0){   //判断文件名和文件大小
      System.out.println("请选择上传的文件！");
     }
     System.out.println("getName()=="+item.getName());
     System.out.println("getFieldName()=="+item.getFieldName());
     item.write(new File("D:/"+item.getName()));      //最后将文件上传到指定的缓存区
     System.out.println("文件上传成功");
   }
  }catch(Exception e){
   e.printStackTrace();
   System.out.println("文件上传错误！");
  }
 }
