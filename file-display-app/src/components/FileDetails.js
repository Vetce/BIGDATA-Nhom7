import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Box,
  Typography,
  Divider,
  Paper,
  Grid,
} from '@mui/material';
import { GetApp as GetAppIcon } from '@mui/icons-material';

const FileDetails = ({ open, file, onClose, onDownload }) => {
  if (!file) return null;

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
  };

  const detailRows = [
    { label: 'Filename', value: file.name },
    { label: 'File Type', value: file.extension.toUpperCase() },
    { label: 'Size', value: formatFileSize(file.size) },
    { label: 'Path', value: file.fullPath },
    {
      label: 'Modified',
      value: new Date(file.mtime).toLocaleString(),
    },
  ];

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>File Details</DialogTitle>
      <DialogContent sx={{ py: 3 }}>
        <Paper sx={{ p: 2, backgroundColor: '#f9f9f9' }}>
          {detailRows.map((row, idx) => (
            <Box key={idx}>
              <Grid container spacing={2} sx={{ mb: 2 }}>
                <Grid item xs={4}>
                  <Typography variant="subtitle2" sx={{ fontWeight: 'bold' }}>
                    {row.label}
                  </Typography>
                </Grid>
                <Grid item xs={8}>
                  <Typography
                    variant="body2"
                    sx={{
                      wordBreak: 'break-word',
                      fontFamily: 'monospace',
                      fontSize: '0.875rem',
                    }}
                  >
                    {row.value}
                  </Typography>
                </Grid>
              </Grid>
              {idx < detailRows.length - 1 && <Divider sx={{ my: 1 }} />}
            </Box>
          ))}
        </Paper>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Close</Button>
        <Button
          onClick={onDownload}
          variant="contained"
          startIcon={<GetAppIcon />}
        >
          Download
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default FileDetails;
