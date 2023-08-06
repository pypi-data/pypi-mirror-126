import locale
import re

import pytest

import graphviz

SOURCE = {'source': 'digraph { hello -> world }\n',
          'filename': 'hello.gv', 'directory': 'test-output',
          'format': 'PNG', 'engine': 'NEATO', 'encoding': 'utf-8'}


@pytest.fixture(scope='module')
def source():
    return graphviz.Source(**SOURCE)


def test_engine(source):
    assert not SOURCE['engine'].islower()

    assert source.engine == SOURCE['engine'].lower()
    with pytest.raises(ValueError, match=r'engine'):
        source.engine = ''


def test_format(source):
    assert not SOURCE['format'].islower()

    assert source.format == SOURCE['format'].lower()
    with pytest.raises(ValueError, match=r'format'):
        source.format = ''


def test_encoding(source):
    assert source.encoding == SOURCE['encoding']

    with pytest.raises(LookupError, match=r'encoding'):
        source.encoding = ''


def test_encoding_none(source):
    source_copy = source.copy()
    source_copy.encoding = None
    assert source_copy.encoding == locale.getpreferredencoding()


def test_init(source):
    assert source.source == SOURCE['source']
    assert source.filename == SOURCE['filename']
    assert source.directory == SOURCE['directory']


def test_init_filename():
    assert graphviz.Source('').filename == 'Source.gv'
    assert type('Named', (graphviz.Source,),
                {'name': 'name'})('').filename == 'name.gv'


def test_str(source):
    assert str(source) == source.source


@pytest.mark.exe
def test_unflatten(source):
    result = source.unflatten()
    assert isinstance(result, graphviz.Source)

    normalized = re.sub(r'\s+', ' ', result.source.strip())
    assert normalized == 'digraph { hello -> world; }'


def test__repr_svg_(mocker, sentinel, source):
    mock_pipe = mocker.patch.object(source, 'pipe', autospec=True,
                                    return_value=sentinel.string)

    assert source._repr_svg_() is sentinel.string

    mock_pipe.assert_called_once_with(format='svg', encoding=source.encoding)


def test_pipe_lines_format(mocker, mock_pipe_lines, source, format_='svg'):
    assert source.format != format_

    assert source.pipe(format=format_) is mock_pipe_lines.return_value

    mock_pipe_lines.assert_called_once_with(source.engine, format_, mocker.ANY,
                                            renderer=None, formatter=None,
                                            input_encoding='utf-8',
                                            quiet=False)
    _, _, data = mock_pipe_lines.call_args.args
    expected_lines = source.source.splitlines(keepends=True)
    assert list(data) == expected_lines


def test_pipe_lines(mocker, mock_pipe_lines, source):
    assert source.pipe() is mock_pipe_lines.return_value

    mock_pipe_lines.assert_called_once_with(source.engine, source.format,
                                            mocker.ANY,
                                            renderer=None, formatter=None,
                                            input_encoding='utf-8',
                                            quiet=False)
    _, _, data = mock_pipe_lines.call_args.args
    expected_lines = source.source.splitlines(keepends=True)
    assert list(data) == expected_lines


def test_filepath(platform, source):
    if platform == 'windows':
        assert source.filepath == 'test-output\\hello.gv'
    else:
        assert source.filepath == 'test-output/hello.gv'


def test_save(mocker, filename='nonfilename', directory='nondirectory'):
    source = graphviz.Source(**SOURCE)
    makedirs = mocker.patch('os.makedirs', autospec=True)
    open_ = mocker.patch('builtins.open', mocker.mock_open())

    assert source.save(filename, directory) == source.filepath

    assert source.filename == filename and source.directory == directory
    makedirs.assert_called_once_with(source.directory, 0o777, exist_ok=True)
    open_.assert_called_once_with(source.filepath, 'w',
                                  encoding=source.encoding)
    assert open_.return_value.write.call_args_list == [mocker.call(source.source)]


def test_render(mocker, sentinel, mock_render, source):
    save = mocker.patch.object(source, 'save', autospec=True,
                               return_value=sentinel.nonfilepath)
    _view = mocker.patch.object(source, '_view', autospec=True)
    remove = mocker.patch('os.remove', autospec=True)

    assert source.render(cleanup=True, view=True) is mock_render.return_value

    save.assert_called_once_with(None, None, skip_existing=None)
    mock_render.assert_called_once_with(source.engine, source.format,
                                        save.return_value,
                                        renderer=None, formatter=None,
                                        quiet=False)
    remove.assert_called_once_with(save.return_value)
    _view.assert_called_once_with(mock_render.return_value, source.format, False)


def test_view(mocker, source):
    mock_render = mocker.patch.object(source, 'render', autospec=True)
    kwargs = {'filename': 'filename', 'directory': 'directory',
              'cleanup': True, 'quiet': True, 'quiet_view': True}

    assert source.view(**kwargs) is mock_render.return_value

    mock_render.assert_called_once_with(view=True, **kwargs)


def test__view_unknown_platform(unknown_platform, source):
    with pytest.raises(RuntimeError, match=r'support'):
        source._view('name', 'png', False)


def test__view(mocker, sentinel, mock_platform, source):
    _view_platform = mocker.patch.object(source, f'_view_{mock_platform}',
                                         autospec=True)

    kwargs = {'quiet': False}

    assert source._view(sentinel.name, 'png', **kwargs) is None

    _view_platform.assert_called_once_with(sentinel.name, **kwargs)


def test_copy(source):
    assert source.copy() is not source
    assert source.copy() is not source.copy()
    assert source.copy().__class__ is source.__class__
    assert source.copy().__dict__ == source.__dict__ == source.copy().__dict__


def test_from_file(tmp_path, filename='hello.gv', directory='source_hello',
                   data='digraph { hello -> world }', encoding='utf-8'):
    lpath = tmp_path / directory
    lpath.mkdir()
    (lpath / filename).write_text(data, encoding=encoding)

    source = graphviz.Source.from_file(filename, str(lpath))
    assert source.encoding == 'utf-8'

    source = graphviz.Source.from_file(filename, str(lpath), encoding=None)
    assert source.encoding == locale.getpreferredencoding()

    renderer = 'xdot'
    formatter = 'core'
    source = graphviz.Source.from_file(filename, str(lpath), encoding=encoding,
                                       renderer=renderer, formatter=formatter)
    assert source.source == data + '\n'
    assert source.filename == filename
    assert source.directory == str(lpath)
    assert source.encoding == encoding
    assert source.renderer == renderer
    assert source.formatter == formatter


def test_source_iter(source):
    source_without_newline = graphviz.Source(source.source + source.source.rstrip())
    lines = list(source_without_newline)

    assert lines == list(source) * 2
