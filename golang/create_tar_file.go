package main

import (
    "fmt"
    "strings"
    "os"
    "path/filepath"
    "archive/tar"
    _"compress/gzip"
    "io"
)

func tarit(source, target string) error {
    filename := filepath.Base(source)
    target = filepath.Join(target,  fmt.Sprintf("%s.tar", filename))
    tarfile, err := os.Create(target)
    if err != nil {
        return err
    }
    defer tarfile.Close()

    tarball := tar.NewWriter(tarfile)
    defer tarball.Close()

    info, err := os.Stat(source)
    if err != nil {
        return err
    }

    var baseDir string
    if info.IsDir() {
        baseDir = filepath.Base(source)
    }

    return filepath.Walk(source,
        func(path string, info os.FileInfo, err error) error {
        header, err := tar.FileInfoHeader(info, info.Name())
        if err != nil {
            return err
        }

        if baseDir != "" {
            header.Name = filepath.Join(baseDir, strings.TrimPrefix(path, source))
        }

        if err := tarball.WriteHeader(header); err != nil {
            return err
        }

        if info.IsDir() {
            return nil
        }

        file, err := os.Open(path)
        if err != nil {
            return err
        }
        defer file.Close()

        _,err = io.Copy(tarball, file)
        return err
    })
}

func main() {
    tarit("/run/tmp/to-be-tar", "/tmp/tar-target")
}
