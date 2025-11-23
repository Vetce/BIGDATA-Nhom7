import React, { useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Box,
  IconButton,
  Tooltip,
  Chip,
  Typography,
} from '@mui/material';
import {
  Visibility as VisibilityIcon,
  Info as InfoIcon,
  GetApp as GetAppIcon,
} from '@mui/icons-material';
import FilePreview from './FilePreview';
import FileDetails from './FileDetails';

const FileExplorer = ({ directory, files, onRefresh }) => {
  const [previewOpen, setPreviewOpen] = useState(false);
  const [detailsOpen, setDetailsOpen] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);

  const handlePreview = (file) => {
    setSelectedFile(file);
    setPreviewOpen(true);
  };

  const handleDetails = (file) => {
    setSelectedFile(file);
    setDetailsOpen(true);
  };

  const handleDownload = (file) => {
    const downloadUrl = `/api/download?path=${encodeURIComponent(file.fullPath)}`;
    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = file.name;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const getFileIcon = (ext) => {
    const icons = {
      csv: '📊',
      json: '{}',
      png: '🖼️',
      jpg: '🖼️',
      h5: '🧠',
      pkl: '📦',
      ipynb: '📓',
    };
    return icons[ext] || '📄';
  };

  const getFileType = (filename) => {
    const ext = filename.split('.').pop().toLowerCase();
    const types = {
      csv: 'Data',
      json: 'Config',
      png: 'Image',
      jpg: 'Image',
      h5: 'Model',
      pkl: 'Pickle',
      ipynb: 'Notebook',
    };
    return types[ext] || 'File';
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
  };

  return (
    <Box>
      <TableContainer component={Paper} sx={{ mt: 2 }}>
        <Table>
          <TableHead>
            <TableRow sx={{ backgroundColor: '#f5f5f5' }}>
              <TableCell sx={{ fontWeight: 'bold', width: '5%' }}>Icon</TableCell>
              <TableCell sx={{ fontWeight: 'bold', width: '30%' }}>Filename</TableCell>
              <TableCell sx={{ fontWeight: 'bold', width: '15%' }}>Type</TableCell>
              <TableCell sx={{ fontWeight: 'bold', width: '15%' }}>Size</TableCell>
              <TableCell sx={{ fontWeight: 'bold', width: '20%' }}>Modified</TableCell>
              <TableCell sx={{ fontWeight: 'bold', width: '15%', textAlign: 'center' }}>
                Actions
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {files.map((file, index) => (
              <TableRow
                key={index}
                hover
                sx={{
                  '&:hover': {
                    backgroundColor: '#f9f9f9',
                  },
                }}
              >
                <TableCell sx={{ fontSize: '1.5rem', textAlign: 'center' }}>
                  {getFileIcon(file.extension)}
                </TableCell>
                <TableCell sx={{ wordBreak: 'break-word' }}>
                  <Typography variant="body2" sx={{ fontFamily: 'monospace' }}>
                    {file.name}
                  </Typography>
                </TableCell>
                <TableCell>
                  <Chip
                    label={getFileType(file.name)}
                    size="small"
                    variant="outlined"
                  />
                </TableCell>
                <TableCell>{formatFileSize(file.size)}</TableCell>
                <TableCell sx={{ fontSize: '0.875rem' }}>
                  {new Date(file.mtime).toLocaleString()}
                </TableCell>
                <TableCell sx={{ textAlign: 'center' }}>
                  <Box sx={{ display: 'flex', gap: 0.5, justifyContent: 'center' }}>
                    {(file.extension === 'csv' ||
                      file.extension === 'json' ||
                      file.extension === 'png') && (
                      <Tooltip title="Preview">
                        <IconButton
                          size="small"
                          onClick={() => handlePreview(file)}
                          color="primary"
                        >
                          <VisibilityIcon fontSize="small" />
                        </IconButton>
                      </Tooltip>
                    )}
                    <Tooltip title="Details">
                      <IconButton
                        size="small"
                        onClick={() => handleDetails(file)}
                        color="info"
                      >
                        <InfoIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>
                    <Tooltip title="Download">
                      <IconButton
                        size="small"
                        onClick={() => handleDownload(file)}
                        color="success"
                      >
                        <GetAppIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>
                  </Box>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <FilePreview
        open={previewOpen}
        file={selectedFile}
        onClose={() => setPreviewOpen(false)}
      />

      <FileDetails
        open={detailsOpen}
        file={selectedFile}
        onClose={() => setDetailsOpen(false)}
        onDownload={() => {
          handleDownload(selectedFile);
          setDetailsOpen(false);
        }}
      />
    </Box>
  );
};

export default FileExplorer;
