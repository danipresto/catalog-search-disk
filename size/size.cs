//Calcular o tamanho do mesmo jeito que windows propriedades


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DiskUsage
{
    class Program
    {
        const string FolderPath = @"D:\contratos\detrance";

        static void Main(string[] args)
        {
           
            var startTime = DateTime.Now;

            Scripting.FileSystemObject fso = new Scripting.FileSystemObject();
            Scripting.Folder folder = fso.GetFolder(FolderPath);
            Int64 dirSize = (Int64)folder.Size;

            TimeSpan span = DateTime.Now.Subtract(startTime);

            System.Console.WriteLine("{1} size: {0}", dirSize/1000000000, FolderPath);
            System.Console.WriteLine("use time: {0}", span);
            System.Console.ReadKey();
        }
    }
}
