import React, { useState, useEffect } from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  CircularProgress,
  Box,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Alert,
} from '@mui/material';

const FilePreview = ({ open, file, onClose }) => {
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (open && file) {
      fetchPreview();
    }
  }, [open, file]);

  const fetchPreview = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch(
        `/api/preview?path=${encodeURIComponent(file.fullPath)}`
      );
      if (!response.ok) {
        throw new Error('Failed to load preview');
      }
      const data = await response.json();
      setPreview(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const renderPreview = () => {
    if (loading) {
      return (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 3 }}>
          <CircularProgress />
        </Box>
      );
    }

    if (error) {
      return <Alert severity="error">{error}</Alert>;
    }

    if (!preview) {
      return <Typography>No preview available</Typography>;
    }

    if (preview.type === 'image') {
      return (
        <Box sx={{ textAlign: 'center' }}>
          <img
            src={preview.data}
            alt="Preview"
            style={{ maxWidth: '100%', maxHeight: '500px' }}
          />
        </Box>
      );
    }

    if (preview.type === 'csv' || preview.type === 'json') {
      return (
        <TableContainer component={Paper} sx={{ maxHeight: 600 }}>
          <Table stickyHeader size="small">
            <TableHead>
              <TableRow sx={{ backgroundColor: '#f5f5f5' }}>
                {preview.headers &&
                  preview.headers.map((header, idx) => (
                    <TableCell key={idx} sx={{ fontWeight: 'bold' }}>
                      {header}
                    </TableCell>
                  ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {preview.data &&
                preview.data.map((row, idx) => (
                  <TableRow key={idx}>
                    {preview.headers &&
                      preview.headers.map((header, colIdx) => (
                        <TableCell key={colIdx} sx={{ fontSize: '0.875rem' }}>
                          {String(row[header] || '').substring(0, 50)}
                        </TableCell>
                      ))}
                  </TableRow>
                ))}
            </TableBody>
          </Table>
        </TableContainer>
      );
    }

    return <Typography>Preview not supported for this file type</Typography>;
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="md" fullWidth>
      <DialogTitle>
        Preview: {file?.name}
      </DialogTitle>
      <DialogContent sx={{ py: 3 }}>
        {renderPreview()}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Close</Button>
      </DialogActions>
    </Dialog>
  );
};

export default FilePreview;
