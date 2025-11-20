import React, { useState, useEffect } from 'react';
import {
  Container,
  Box,
  Typography,
  CircularProgress,
  Alert,
  Tabs,
  Tab,
  Paper,
} from '@mui/material';
import FileExplorer from './components/FileExplorer';
import './App.css';

function App() {
  const [files, setFiles] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState(0);

  useEffect(() => {
    fetchFiles();
  }, []);

  const fetchFiles = async () => {
    try {
      setLoading(true);
      const response = await fetch('/api/files');
      if (!response.ok) {
        throw new Error('Failed to fetch files');
      }
      const data = await response.json();
      setFiles(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const directories = Object.keys(files).sort();

  const handleTabChange = (event, newValue) => {
    setActiveTab(newValue);
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom sx={{ fontWeight: 'bold', mb: 2 }}>
          📁 BIGDATA File Explorer
        </Typography>
        <Typography variant="subtitle1" color="textSecondary">
          Browse and manage files from your data directories
        </Typography>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          Error: {error}
        </Alert>
      )}

      {loading ? (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
          <CircularProgress />
        </Box>
      ) : directories.length === 0 ? (
        <Alert severity="info">No files found in the configured directories.</Alert>
      ) : (
        <Paper sx={{ mb: 3 }}>
          <Tabs
            value={activeTab}
            onChange={handleTabChange}
            variant="scrollable"
            scrollButtons="auto"
            sx={{ borderBottom: 1, borderColor: 'divider' }}
          >
            {directories.map((dir, index) => (
              <Tab
                key={index}
                label={`${dir} (${files[dir].length})`}
                sx={{ textTransform: 'none', fontSize: '1rem' }}
              />
            ))}
          </Tabs>

          <Box sx={{ p: 3 }}>
            {directories.map((dir, index) => (
              <div key={index} hidden={activeTab !== index}>
                <FileExplorer
                  directory={dir}
                  files={files[dir]}
                  onRefresh={fetchFiles}
                />
              </div>
            ))}
          </Box>
        </Paper>
      )}
    </Container>
  );
}

export default App;
